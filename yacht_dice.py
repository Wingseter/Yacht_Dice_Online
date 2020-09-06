import pygame
import menus
from loader import MAIN

# pygame 시작
pygame.init()
clock = pygame.time.Clock()

# pygame 디스플레이 설정
win = pygame.display.set_mode((1200, 1000))
pygame.display.set_caption("Yacht_Dice")
pygame.display.set_icon(MAIN.ICON)

running = True

# x, y, width, height
title = (200, 100, 300, 100)
offln = (600, 450, 300, 100)
onln = (600, 550, 300, 100)
opt = (600, 650, 300, 100)
qit = (600, 750, 300, 100)


# 메인 메뉴
def showMain():
    win.blit(MAIN.TITLE, title[:2])
    win.blit(MAIN.OFFLINE, offln[:2])
    win.blit(MAIN.ONLINE, onln[:2])
    win.blit(MAIN.OPTION, opt[:2])
    win.blit(MAIN.QUIT, qit[:2])

# 게임 메인 루프
while running:
    clock.tick(30)
    showMain()
    x, y = pygame.mouse.get_pos()

    if offln[0] < x < sum(offln[::2]) and offln[1] < y < sum(offln[1::2]):
        win.blit(MAIN.OFFLINE_H, offln[:2])
    elif onln[0] < x < sum(onln[::2]) and onln[1] < y < sum(onln[1::2]):
        win.blit(MAIN.ONLINE_H, onln[:2])
    elif opt[0] < x < sum(opt[::2]) and opt[1] < y < sum(opt[1::2]):
        win.blit(MAIN.OPTION_H, opt[:2])
    elif qit[0] < x < sum(qit[::2]) and qit[1] < y < sum(qit[1::2]):
        win.blit(MAIN.QUIT_H, qit[:2])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if onln[0] < x < sum(onln[::2]) and onln[1] < y < sum(onln[1::2]):
                menus.onlinemenu(win)

    pygame.display.flip()

pygame.quit()