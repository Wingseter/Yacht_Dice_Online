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

# 게임 메인 루프
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()