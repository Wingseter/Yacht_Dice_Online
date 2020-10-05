import pygame
from game.onlinelib.sockutils import *
from loader import ONLINE

def showLoading(win, errcode= -1):
    pygame.draw.rect(win, (255, 255, 255), (300, 500, 600, 60))
    pygame.draw.rect(win, (0,0,0), (303, 503, 594, 54))

    if errcode == -1:
        win.blit(ONLINE.TRYCONN, (303, 504))
        pygame.display.update()
        return 
    
    win.blit(ONLINE.ERR[errcode], (303, 504))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return

def showLobby(win, key, playerlist):
    win.fill((0, 0, 0))
    
    win.blit(ONLINE.LOBBY, (100, 14))
