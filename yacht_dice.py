import pygame
from loader import MAIN

# pygame 시작
pygame.init()
clock = pygame.time.Clock()

# pygame 디스플레이 설정
win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Yacht_Dice")
pygame.display.set_icon(MAIN.ICON)

running = True

title = (100, 100, 120, 40)
offln = (550, 450, 120, 40)
onln = (550, 550, 120, 40)
opt = (550, 650, 120, 40)
qit = (550, 750, 120, 40)


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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if onln[0] < x < sum(onln[::2]) and onln[1] < y < sum(onln[1::2]):
                menus.onlinemenu(win)

    pygame.display.flip()

pygame.quit()