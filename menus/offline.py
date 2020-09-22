import pygame
import time
import random
from tools.utils import emptyRoundRect

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
win = pygame.display.set_mode((1200, 750), 0, 32)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_COLOR = (127, 127, 127)

#win = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
#pygame.display.set_caption('Yacht Dice Game')


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
    win.fill((100, 0, 0))

    # 배경
    emptyRoundRect(win, (255, 255, 255), (20, 100, 1150, 630), 14, 4)

    for i in range(0, 11):
        time.sleep(0.1)

        if i == 10:
            # 10번 굴리고 반환
            return

        # 화면 업데이트 (총 10번 진행)
        for dice in dices:
            dice.draw(win)
        pygame.display.update()


def main(win):

    while True:
        dices = []
        clock.tick(60)
        for event in pygame.event.get():

            # 턴넘기기
            # if state == "player_turn":
            # 플레이어 턴일때,
            # elif state == "enemy_turn":
            # 상대방 턴일때,
            # elif state == "paused":
            # 일시정지 상태일때.

            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONUP:
                # 마우스 클릭을 했을때
                dices = [
                    # 주사위 객체들
                    Dice(130, 230, 100, 100),
                    Dice(330, 230, 100, 100),
                    Dice(530, 230, 100, 100),
                    Dice(730, 230, 100, 100),
                    Dice(930, 230, 100, 100)
                ]
                redrawGameWindow(dices)
