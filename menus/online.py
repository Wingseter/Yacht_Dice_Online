import pygame
from tools.utils import emptyRoundRect

def showScreen(win):
    win.fill((0,0,0))
    emptyRoundRect(win, (255,255,255), (120, 10, 260, 70), 20, 4)
    

def main(win):
    clock = pygame.time.Clock()
    print("clicked")

    while True:
        clock.tick(24)
        showScreen(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

        pygame.display.update()