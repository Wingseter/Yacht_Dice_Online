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
        self.status = 'stopped'

    def roll(self, win):
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

       # 주사위 애니메이션
        self.x += random.randint(-10, 10)
        self.y += random.randint(-10, 10)


def redrawGameWindow(dices):

    for i in range(0, 11):
        time.sleep(0.1)
        win.fill((100, 0, 0))
        emptyRoundRect(win, (255, 255, 255), (20, 100, 1150, 630), 14, 4)
        if i == 10:
            # 10번 굴리고 반환
            return

        # 화면 업데이트 (총 10번 진행)
        for dice in dices:
            if dice.status == 'rolling':
                dice.roll(win)
        pygame.display.update()


def main(win):

    while True:
        dices = []
        clock.tick(60)

        # 주사위 객체들
        dices = [
            Dice(130, 230, 100, 100),
            Dice(330, 230, 100, 100),
            Dice(530, 230, 100, 100),
            Dice(730, 230, 100, 100),
            Dice(930, 230, 100, 100)
        ]

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
                for dice in dices:
                    dice.status = 'rolling'
                redrawGameWindow(dices)

                # 다시 주사위 상태를 stopped로 변경
                for dice in dices:
                    dice.status = 'stopped'
