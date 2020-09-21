import pygame
import time
import random

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

SC_WIDTH = 600
SC_HEIGHT = 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_COLOR = (127, 127, 127)

win = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
pygame.display.set_caption('Yacht Dice Game')


class Dice(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # self.roll_time = 0
        self.side = 0

    def draw(self, win):

        pygame.draw.rect(win, WHITE, (self.x, self.y, 100, 100))

        # myfont = pygame.font.SysFont('Comicsans', 30)
        # mytext = myfont.render(str(side), 1, BLACK)
        # win.blit(mytext, (10, 10))

        self.side = random.randint(1, 6)
        if self.side == 1 or self.side == 3 or self.side == 5:
            pygame.draw.circle(win, BLACK, (self.x + 50, self.y + 50), 8, 8)
        if self.side == 4 or self.side == 5 or self.side == 6:
            pygame.draw.circle(win, BLACK, (self.x + 20, self.y + 20), 8, 8)
        if self.side == 6:
            pygame.draw.circle(win, BLACK, (self.x + 20, self.y + 50), 8, 8)
        if self.side == 2 or self.side == 3 or self.side == 4 or self.side == 5 or self.side == 6:
            pygame.draw.circle(win, BLACK, (self.x + 20, self.y + 80), 8, 8)
        if self.side == 2 or self.side == 3 or self.side == 4 or self.side == 5 or self.side == 6:
            pygame.draw.circle(win, BLACK, (self.x + 80, self.y + 20), 8, 8)
        if self.side == 6:
            pygame.draw.circle(win, BLACK, (self.x + 80, self.y + 50), 8, 8)
        if self.side == 4 or self.side == 5 or self.side == 6:
            pygame.draw.circle(win, BLACK, (self.x + 80, self.y + 80), 8, 8)


def redrawGameWindow(dices):
    win.fill(BG_COLOR)

    for i in range(0, 11):
        time.sleep(0.1)

        if i == 10:
            # 10번 굴리고 반환
            return

        # 화면 업데이트 (총 10번 진행)
        for dice in dices:
            dice.draw(win)
        pygame.display.update()


run = True

while run:
    dices = []
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            # 마우스 클릭을 했을때
            dices = [
                # 주사위 객체들
                Dice(30, 30, 100, 100),
                Dice(140, 30, 100, 100),
                Dice(250, 30, 100, 100),
                Dice(360, 30, 100, 100),
                Dice(470, 30, 100, 100)
            ]
            redrawGameWindow(dices)
