import pygame
from tools.utils import emptyRoundRect
from tools.textBox import textBox
from loader import ONLINEMENU as ONLINE, FONT

def showScreen(win):
    win.fill((100,0,0))
    
    emptyRoundRect(win, (255, 255, 255), (20, 100, 1150, 630), 14, 4)
    win.blit(ONLINE.HEAD, (30, -20))

    for cnt, i in enumerate(ONLINE.TEXT):
        win.blit(i, (40, 100 + cnt * 18))    
    

def main(win):
    clock = pygame.time.Clock()
    pg = True

    serverInput = textBox(FONT, (0, 0, 0), (300, 450, 200, 35))
    while True:
        clock.tick(24)
        showScreen(win)

        if pg:
            pygame.draw.rect(win, (255, 255, 255), (298, 448, 204, 39))
            serverInput.draw(win)

        for event in pygame.event.get():
            if pg:
                serverInput.push(event)

            if event.type == pygame.QUIT:
                return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if pg:
                    pass
                else:
                    pass

        pygame.display.update()