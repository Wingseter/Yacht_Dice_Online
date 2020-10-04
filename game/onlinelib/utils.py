import pygame

from loader import ONLINE

def showLoading(win, errcode= -1):
    pygame.draw.rect(win, (255, 255, 255), (200, 500, 600, 60))
    pygame.draw.rect(win, (0,0,0), (203, 523, 694, 54))

    if errcode == -1:
        win.blit(ONLINE.TRYCONN, (135, 240))
        pygame.display.update()
        return 
    
    win.blit(ONLINE.ERR[errcode], (100, 240))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
