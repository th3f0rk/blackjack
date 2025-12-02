from blackjack.engine.engine import GameEngine
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("BlackJack Wizard")
font = pygame.font.SysFont(None, 36)
engine = GameEngine()
game_state = 'waiting'
running = True

while running:
    screen.fill((0, 100, 0))
    lines = []
    lines.append(f"Game State: {game_state}")
    if game_state != 'waiting':
        player_cards_str = ', '.join(str(card) for card in engine.player.hand)
        player_line = f'Player Cards: [{player_cards_str}]  Total: {engine.player.hand_total}'
        lines.append(player_line)

        if engine.hide_card and game_state == 'player_turn':
            dealer_first = str(engine.dealer.hand[0])
            dealer_line = f"Dealer Cards: [{dealer_first}, ?]  Total: ?"
        else:
            dealer_cards_str = ", ".join(str(card) for card in engine.dealer.hand)
            dealer_line = f"Dealer Cards: [{dealer_cards_str}]  Total: {engine.dealer.hand_total}"

        lines.append(dealer_line)

    if game_state == 'end' and engine.isresult is not None:
        result_line = f"Result: {engine.isresult}"
        lines.append(result_line)

    if game_state == 'waiting':
        instructions = "Press SPACE to deal a hand."
    elif game_state == 'player_turn':
        instructions = "Your turn: H = Hit, S = Stand, D = Double."
    elif game_state == 'end':
        instructions = "Hand over. Press SPACE to deal again."
    else:
        instructions = ""
    lines.append(instructions)

    y = 50
    for text in lines:
        text_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, (50, y))
        y += 40

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and (game_state == 'waiting' or game_state == 'end'):
                engine.start_round()
                if engine.turn == 'player':
                    game_state = 'player_turn'
                else:
                    game_state = 'end'
            #hit logic
            if event.key == pygame.K_h and game_state == 'player_turn':
                engine.player_hit()
                if engine.turn == None: #this means the player busted
                    game_state = 'end'
            #stand
            if event.key == pygame.K_s and game_state == 'player_turn':
                engine.player_stand()
                if engine.turn == None: #this means the dealer busted
                    game_state = 'end'
            #double logic
            if event.key == pygame.K_d and game_state == 'player_turn':
                engine.player_double()
                if engine.turn == None: #this means the player busted on the double
                    game_state = 'end'
                else:
                    engine.run_dealer()
                    if engine.turn == None: #this means the dealer busted
                        game_state = 'end'

    pygame.display.flip()
    clock.tick(60)

pygame.quit()



