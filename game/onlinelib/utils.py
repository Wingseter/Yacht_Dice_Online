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

# 게임 요청
def request(win, key, sock=None):
    if sock is None:
        pygame.draw.rect(win, (0, 0, 0), (240, 260, 650, 200))
        pygame.draw.rect(win, (255, 255, 255), (240, 260, 650, 200), 4)

        win.blit(ONLINE.MSG2[0], (265, 275))
        win.blit(ONLINE.MSG2[1], (500, 275))
        win.blit(ONLINE.MSG2[2], (265, 320))
        putNum(win, key, (400, 275))

        win.blit(ONLINE.OK, (380, 375))
        win.blit(ONLINE.NO, (610, 375))
        pygame.draw.rect(win, (255, 255, 255), (370, 380, 100, 50), 2)
        pygame.draw.rect(win, (255, 255, 255), (600, 380, 100, 50), 2)

        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 380 < event.pos[1] < 430:
                        if 370 < event.pos[0] < 470:
                            return True
                        elif 600 < event.pos[0] < 700:
                            return False
    else:
        pygame.draw.rect(win, (0, 0, 0), (240, 260, 650, 200))
        pygame.draw.rect(win, (255, 255, 255), (240, 260, 650, 200), 4)

        win.blit(ONLINE.MSG1[0], (265, 275))
        win.blit(ONLINE.MSG1[1], (265, 320))
        win.blit(ONLINE.MSG1[2], (265, 365))

        pygame.display.flip()
        while True:
            if readable():
                msg = read()
                if msg == "close":
                    return None

                elif msg == "start":
                    write(sock, "ready")
                    return True

                elif msg == "nostart":
                    write(sock, "pass")
                    return False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    write(sock, "quit")
                    return None