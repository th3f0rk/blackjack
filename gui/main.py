from blackjack.engine.engine import GameEngine
from blackjack.assets import asset
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
asset.assets()
clock = pygame.time.Clock()
pygame.display.set_caption("BlackJack Wizard")
font = pygame.font.SysFont(None, 36)
engine = GameEngine()
game_state = 'waiting'
running = True

# Bankroll / betting
bankroll = 1000
current_bet = 0      # what the player is setting with chips
active_bet = 0       # bet actually in play for the current hand
round_num = 0
payout_done = False  # to ensure we only pay out once per hand

# Dealer timing control
dealer_timer = 0
DEALER_DELAY = 1000  # ms between dealer actions
dealer_phase = 0     # 0 = flip hole card, 1+ = run dealer steps

width, height = screen.get_size()
margin = 40
menu_margin = 20
chip_margin = 20
wizard_margin = 20
button_spacing = 20
chip_spacing = 125
bottom_y = height - margin

deal_rect = asset.deal_img.get_rect()
stand_rect = asset.deal_img.get_rect()
double_rect = asset.deal_img.get_rect()
hit_rect = asset.deal_img.get_rect()

deal_rect.bottomright = (width - margin, bottom_y)
double_rect.bottomright = (width - margin, deal_rect.top - button_spacing)
stand_rect.bottomright = (deal_rect.left - button_spacing, bottom_y)
hit_rect.bottomright = (deal_rect.left - button_spacing, stand_rect.top - button_spacing)

chip5_rect = asset.chip_5.get_rect()
chip10_rect = asset.chip_10.get_rect()
chip25_rect = asset.chip_25.get_rect()

chip5_rect.bottomleft = (chip_margin, bottom_y)
chip10_rect.bottomleft = (chip5_rect.right - chip_spacing, bottom_y)
chip25_rect.bottomleft = (chip10_rect.right - chip_spacing, bottom_y)

menu_rect = asset.menu_img.get_rect()
wizard_rect = asset.wizard_img.get_rect()
menu_rect.topright = (width - menu_margin, menu_margin)
wizard_rect.topright = (width - (wizard_margin / 2), menu_rect.bottom + wizard_margin)

dealer_anchor = (width // 2, int(height * 0.23))
player_anchor = (width // 2, int(height * 0.69))

CARD_SPACING = 40


def get_card_image(card):
    """
    card is a (rank, value) tuple, e.g. ('K', 10), ('A', 11), ('nine', 9)
    We only care about rank to pick the correct sprite.
    """
    rank, value = card

    if rank == 'A':
        return asset.card_ace
    if rank == 'K':
        return asset.card_king
    if rank == 'Q':
        return asset.card_queen
    if rank == 'J':
        return asset.card_jack
    if rank == 'ten':
        return asset.card_ten
    if rank == 'nine':
        return asset.card_nine
    if rank == 'eight':
        return asset.card_eight
    if rank == 'seven':
        return asset.card_seven
    if rank == 'six':
        return asset.card_six
    if rank == 'five':
        return asset.card_five
    if rank == 'four':
        return asset.card_four
    if rank == 'three':
        return asset.card_three
    if rank == 'two':
        return asset.card_two

    # Fallback – shouldn't happen, but avoids crashing
    return asset.card_back


def draw_hand(cards, anchor_pos, hide_first=False):
    """
    cards: list of (rank, value) tuples from engine.player.hand / engine.dealer.hand
    anchor_pos: (x, y) center of the hand
    hide_first: if True, first card is drawn face-down
    """
    if not cards:
        return

    x_center, y_center = anchor_pos
    n = len(cards)

    for i, card in enumerate(cards):
        offset_index = i - (n - 1) / 2
        card_x = x_center + int(offset_index * CARD_SPACING)
        card_y = y_center

        if hide_first and i == 0:
            img = asset.card_back
        else:
            img = get_card_image(card)

        rect = img.get_rect(center=(card_x, card_y))
        screen.blit(img, rect)


while running:
    screen.fill((0, 100, 0))
    lines = []

    # HUD: bankroll / bet / round
    lines.append(f"Bankroll: {bankroll}")
    lines.append(f"Current Bet: {current_bet}")
    lines.append(f"Round: {round_num}")

    # instructions / result text
    if game_state == 'waiting':
        instructions = "Click a chip to set your bet, then click DEAL."
    elif game_state == 'player_turn':
        instructions = "Your turn: use HIT / STAND / DOUBLE."
    elif game_state == 'dealer_turn':
        instructions = "Dealer is playing..."
    elif game_state == 'end':
        instructions = "Hand over. Click DEAL for the next hand."
    else:
        instructions = ""

    lines.append(instructions)

    if engine.isresult is not None and game_state == 'end':
        lines.append(f"Result: {engine.isresult}")

    # draw HUD text
    y = 20
    for text in lines:
        text_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, (50, y))
        y += 30

    # chips
    screen.blit(asset.chip_5, chip5_rect)
    screen.blit(asset.chip_10, chip10_rect)
    screen.blit(asset.chip_25, chip25_rect)

    # buttons
    screen.blit(asset.deal_img, deal_rect)
    screen.blit(asset.double_img, double_rect)
    screen.blit(asset.stand_img, stand_rect)
    screen.blit(asset.hit_img, hit_rect)

    # menu + wizard
    screen.blit(asset.menu_img, menu_rect)
    screen.blit(asset.wizard_img, wizard_rect)

    # cards
    if game_state != 'waiting':
        # use ONLY engine.hide_card to decide if dealer’s first card is face-down
        dealer_hide_first = engine.hide_card
        draw_hand(engine.dealer.hand, dealer_anchor, hide_first=dealer_hide_first)
        draw_hand(engine.player.hand, player_anchor, hide_first=False)

    # ---- Payout logic: apply once when a hand finishes ----
    if game_state == "end" and not payout_done and engine.isresult is not None:
        if engine.isresult == "Win":
            bankroll += active_bet
        elif engine.isresult == "Loss":
            bankroll -= active_bet
        # Push: no change
        payout_done = True

    # timed dealer logic
    if game_state == "dealer_turn":
        now = pygame.time.get_ticks()
        if now - dealer_timer >= DEALER_DELAY:
            dealer_timer = now

            if dealer_phase == 0:
                # First step: just flip the dealer's hole card
                engine.hide_card = False
                dealer_phase = 1
            else:
                # Subsequent steps: run one dealer AI step
                engine.run_dealer_step()
                if engine.turn is None:
                    game_state = "end"

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos

            # ---- Chip clicks: only allowed before a hand starts or after it ends ----
            if game_state in ("waiting", "end"):
                if chip5_rect.collidepoint(mouse_pos):
                    if bankroll >= 5:
                        current_bet = 5
                elif chip10_rect.collidepoint(mouse_pos):
                    if bankroll >= 10:
                        current_bet = 10
                elif chip25_rect.collidepoint(mouse_pos):
                    if bankroll >= 25:
                        current_bet = 25

            # DEAL: start a new round from waiting or end
            if deal_rect.collidepoint(mouse_pos):
                if game_state in ("waiting", "end") and current_bet > 0 and bankroll >= current_bet:
                    engine.start_round()
                    game_state = "player_turn"
                    dealer_phase = 0  # reset for future dealer turn
                    payout_done = False
                    round_num += 1
                    # lock in the bet for this hand
                    active_bet = current_bet

            if game_state == "player_turn":
                # HIT
                if hit_rect.collidepoint(mouse_pos):
                    engine.player_hit()
                    if engine.turn is None:
                        game_state = "end"

                # STAND
                if stand_rect.collidepoint(mouse_pos):
                    engine.player_stand()
                    game_state = "dealer_turn"
                    dealer_phase = 0
                    dealer_timer = pygame.time.get_ticks()

                # DOUBLE
                if double_rect.collidepoint(mouse_pos):
                    engine.player_double()
                    if engine.turn is None:
                        # busted immediately
                        game_state = "end"
                    else:
                        # dealer must now play
                        game_state = "dealer_turn"
                        dealer_phase = 0
                        dealer_timer = pygame.time.get_ticks()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

