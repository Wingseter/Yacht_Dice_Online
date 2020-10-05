import pygame
from game.onlinelib.sockutils import *
from loader import ONLINE, putLargeNum, putNum

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
    win.fill((0, 100, 0))
    
    win.blit(ONLINE.LOBBY, (10, -15))
    win.blit(ONLINE.LIST, (50, 100))
    win.blit(ONLINE.REFRESH, (450, 120))
    pygame.draw.line(win, (255, 255, 255), (20, 114), (800, 114), 3)
    
    if not playerlist:
        win.blit(ONLINE.EMPTY, (100, 220))
    
    for cnt, player in enumerate(playerlist):
        pkey, stat = int(player[:4]), player[4]
        yCord = 170 + cnt * 30
        
        putNum(win, cnt + 1, (70, yCord))
        win.blit(ONLINE.DOT, (86, yCord))
        win.blit(ONLINE.PLAYER, (102, yCord))
        putNum(win, pkey, (230, yCord))
        if stat == "a":
            win.blit(ONLINE.ACTIVE, (350, yCord))
        elif stat == "b":
            win.blit(ONLINE.BUSY, (350, yCord))
        pygame.draw.rect(win, (255, 255, 255), (70, yCord + 2, 700, 40), 2)
        win.blit(ONLINE.REQ, (500, yCord))

    win.blit(ONLINE.YOUARE, (100, 630))
    pygame.draw.rect(win, (255, 255, 255), (30, 150, 1100, 500), 3)
    win.blit(ONLINE.PLAYER2, (460, 650))
    putLargeNum(win, key, (650, 650))

    pygame.display.update()