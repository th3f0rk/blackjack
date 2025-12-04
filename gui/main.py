from blackjack.engine.engine import GameEngine
from blackjack.assets import asset
import pygame
import random
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
chip_spacing = 200
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


def get_card_image(value):
    if value == 11 or value == 1:
        return asset.card_ace
    if value == 10:
        return asset.card_ten
    if value == 9:
        return asset.card_nine
    if value == 8:
        return asset.card_eight
    if value == 7:
        return asset.card_seven
    if value == 6:
        return asset.card_six
    if value == 5:
        return asset.card_five
    if value == 4:
        return asset.card_four
    if value == 3:
        return asset.card_three
    if value == 2:
        return asset.card_two
    return asset.card_back


def draw_hand(values, anchor_pos, hide_first=False):
    if not values:
        return

    x_center, y_center = anchor_pos
    n = len(values)

    for i, value in enumerate(values):
        offset_index = i - (n - 1) / 2
        card_x = x_center + int(offset_index * CARD_SPACING)
        card_y = y_center

        if hide_first and i == 0:
            img = asset.card_back
        else:
            img = get_card_image(value)

        rect = img.get_rect(center=(card_x, card_y))
        screen.blit(img, rect)


while running:
    screen.fill((0, 100, 0))
    lines = []

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

    # instructions / result text
    if game_state == 'waiting':
        instructions = "Click DEAL to start a hand."
    elif game_state == 'player_turn':
        instructions = "Your turn: use HIT / STAND / DOUBLE."
    elif game_state == 'dealer_turn':
        instructions = "Dealer is playing..."
    elif game_state == 'end':
        instructions = "Hand over. Click DEAL for the next hand."
    else:
        instructions = ""

    lines.append(instructions)

    if engine.isresult is not None:
        lines.append(f"Result: {engine.isresult}")

    y = 50
    for text in lines:
        text_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, (50, y))
        y += 40

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

            # DEAL: start a new round from waiting or end
            if deal_rect.collidepoint(mouse_pos):
                if game_state in ("waiting", "end"):
                    engine.start_round()
                    game_state = "player_turn"
                    dealer_phase = 0  # reset for future dealer turn

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

