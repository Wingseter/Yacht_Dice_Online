import pygame

def showScreen(win):
    win.fill((0,0,0))

def main(win):
    clock = pygame.time.Clock()

    while True:
        clock.tick(24)
        showScreen(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

        pygame.display.update()