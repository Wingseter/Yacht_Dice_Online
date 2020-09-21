import pygame
import menus
import os
from loader import MAIN

pygame.init()
clock = pygame.time.Clock()

win = pygame.display.set_mode((1200, 750), 0, 32)

win.fill((255, 209, 155))
    clock.tick(30)

    x, y = pygame.mouse.get_pos()
    if offln[0] < x < sum(offln[::2]) and offln[1] < y < sum(offln[1::2]):
        win.blit(MAIN.OFFLINE_H, offln[:2])
    elif onln[0] < x < sum(onln[::2]) and onln[1] < y < sum(onln[1::2]):
        win.blit(MAIN.ONLINE_H, onln[:2])
    elif opt[0] < x < sum(opt[::2]) and opt[1] < y < sum(opt[1::2]):
        win.blit(MAIN.OPTION_H, opt[:2])
    elif qit[0] < x < sum(qit[::2]) and qit[1] < y < sum(qit[1::2]):
        win.blit(MAIN.QUIT_H, qit[:2])

while True:
    def draw_button(button, screen):

     pygame.draw.rect(screen, button['color'], button['rect'])
     screen.blit(button['text'], button['text rect'])

    def create_button(x, y, w, h, text, callback, ):

          
    text_surf = FONT.render(text, True, WHITE)
    button_rect = pygame.Rect(x, y, w, h)
    text_rect = text_surf.get_rect(center=button_rect.center)
    button = {
        'rect': button_rect,
        'text': text_surf,
        'text rect': text_rect,
        'color': INACTIVE_COLOR,
        'callback': callback,
        }
    return button


     def printing_dice():
        nonlocal dice
        nonlocal round_count
        dice = None
        dice = dice_func.dice()
        round_count += 1


        pygame.draw.rect(screen, BLACK, [10, 10, 880, 580], 6)

        pygame.draw.line(screen, BLACK, [220, 10], [220, 590], 3)
        pygame.draw.line(screen, BLACK, [440, 10], [440, 590], 3)
        pygame.draw.line(screen, BLACK, [660, 10], [660, 590], 3)

        pygame.draw.line(screen, BLACK, [10, 92],  [890, 92],  3)
        pygame.draw.line(screen, BLACK, [10, 174], [890, 174], 3)
        pygame.draw.line(screen, BLACK, [10, 256], [890, 256], 3)
        pygame.draw.line(screen, BLACK, [10, 338], [890, 338], 3)
        pygame.draw.line(screen, BLACK, [10, 420], [890, 420], 3)
        pygame.draw.line(screen, BLACK, [10, 502], [890, 502], 3)


        pygame.display.update()
        clock.tick(30)
