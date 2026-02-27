import pygame
import os

def scale(img, factor):
    w, h = img.get_size()
    return pygame.transform.scale(img, (int(w * factor), int(h * factor)))

ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'png')

def load_image(filename):
    path = os.path.join(ASSETS_DIR, filename)
    image = pygame.image.load(path).convert_alpha()
    return image

#buttons    
deal_img = None
stand_img = None
double_img = None
menu_img = None
hit_img = None
wizard_img = None

#chips
chip_5 = None
chip_10 = None
chip_25 = None

#cards
card_ace = None
card_king = None
card_queen = None
card_jack = None
card_ten = None
card_nine = None
card_eight = None
card_seven = None
card_six = None
card_five = None
card_four = None
card_three = None
card_two = None
card_back = None

def assets():
    global deal_img, stand_img, double_img, menu_img, hit_img, wizard_img
    global chip_5, chip_10, chip_25
    global card_ace, card_king, card_queen, card_jack, card_ten, card_nine, card_eight, card_seven, card_six, card_five, card_four, card_three, card_two, card_back

    deal_img = load_image('deal_button.png')
    hit_img = load_image('hit_button.png')
    double_img = load_image('double_button.png')
    stand_img = load_image('stand_button.png')

    chip_5 = load_image('bet_5.png')
    chip_10 = load_image('bet_10.png')
    chip_25 = load_image('bet_25.png')

    card_ace = load_image('ace.png')
    card_king = load_image('king.png')
    card_queen = load_image('queen.png')
    card_jack = load_image('jack.png')
    card_ten = load_image('ten.png')
    card_nine = load_image('nine.png')
    card_eight = load_image('eight.png')
    card_seven = load_image('seven.png')
    card_six = load_image('six.png')
    card_five = load_image('five.png')
    card_four = load_image('four.png')
    card_three = load_image('three.png')
    card_two = load_image('two.png')
    card_back = load_image('back.png')

    menu_img = load_image('menu_button.png')
    wizard_img = load_image('wizard.png')
    
    #scaling
    chip_5 = scale(chip_5, 2)
    chip_10 = scale(chip_10, 2)
    chip_25 = scale(chip_25, 2)
    wizard_img = scale(wizard_img, 3)
    card_ace = scale(card_ace, 2)
    card_king = scale(card_king, 2)
    card_queen = scale(card_queen, 2)
    card_jack = scale(card_jack, 2)
    card_ten = scale(card_ten, 2)
    card_nine = scale(card_nine, 2)
    card_eight = scale(card_eight, 2)
    card_seven = scale(card_seven, 2)
    card_six = scale(card_six, 2)
    card_five = scale(card_five, 2)
    card_four = scale(card_four, 2)
    card_three = scale(card_three, 2)
    card_two = scale(card_two, 2)
    card_back = scale(card_back, 2)

