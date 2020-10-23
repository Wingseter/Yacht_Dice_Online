import pygame
from tools.utils import emptyRoundRect
from tools.textBox import textBox
from tools import sound
from loader import ONLINEMENU as ONLINE, FONT

def showScreen(win):
    win.fill((100,0,0))
    
    # 배경
    emptyRoundRect(win, (255, 255, 255), (20, 100, 1150, 630), 14, 4)
    win.blit(ONLINE.HEAD, (30, -20))

    # This is online Menu
    win.blit(ONLINE.ENTER, (400, 300, 100, 40))
    for cnt, i in enumerate(ONLINE.TEXT):
        win.blit(i, (40, 100 + cnt * 18))

    # CONNECT
    emptyRoundRect(win, (255,255,255), (450, 400, 300, 80))
    win.blit(ONLINE.CONNECT, (500, 400))


def main(win, LOAD):
    clock = pygame.time.Clock()

    serverInput = textBox(FONT, (0, 0, 0), (350, 350, 500, 40))
    while True:
        clock.tick(24)
        showScreen(win)
        
        pygame.draw.rect(win, (255, 255, 255), (348, 348, 504, 44))
        serverInput.draw(win)

        for event in pygame.event.get():
            serverInput.push(event)

            if event.type == pygame.QUIT:
                return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # CONNECT 버튼 클릭
                if 450 < x < 750 and 400 < y < 480:
                    sound.play_click(LOAD)
                    return serverInput.text

        pygame.display.update()