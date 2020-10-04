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
myfont = pygame.font.SysFont('Comicsans', 30)
state = 'player_turn'
turn_cnt = 0

# win = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
# pygame.display.set_caption('Yacht Dice Game')


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

        # 만약 멈춰 있는 상태라면 굴리는 상태로 변환
        if self.status == 'stopped':
            self.status = 'rolling'

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

    # 10번 굴리고 반환
    for i in range(0, 11):
        time.sleep(0.1)
        win.fill((100, 0, 0))
        emptyRoundRect(win, (255, 255, 255), (20, 100, 1150, 630), 14, 4)

        # 화면 업데이트 (총 10번 진행)
        for dice in dices:
            dice.roll(win)
            if i == 10:
                dice.status = 'stopped'
            mytext1 = myfont.render(str(dice.side), 1, BLACK)
            win.blit(mytext1, (dice.x + 20, 10))
            mytext2 = myfont.render(str(dice.status), 1, BLACK)
            win.blit(mytext2, (dice.x + 20, 30))
            mytext3 = myfont.render(str(state), 1, BLACK)
            win.blit(mytext3, (20, 10))
            pygame.display.update()

        if i == 10:
            return


def main(win):
    global state
    global turn_cnt

    while True:
        dices = []
        clock.tick(60)

        # 주사위 객체들
        dices = [
            Dice(550, 330, 90, 90),
            Dice(660, 330, 90, 90),
            Dice(770, 330, 90, 90),
            Dice(880, 330, 90, 90),
            Dice(990, 330, 90, 90)
        ]

        for event in pygame.event.get():

            # 턴넘기기
            if state == 'player_turn':
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.MOUSEBUTTONUP:
                    turn_cnt += 1
                    # 마우스 클릭을 했을때
                    for dice in dices:
                        dice.status = 'stopped'
                    redrawGameWindow(dices)
                    if turn_cnt == 3:
                        turn_cnt = 0
                        state = 'enemy_turn'
            elif state == "enemy_turn":
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.MOUSEBUTTONUP:
                    turn_cnt += 1
                    # 마우스 클릭을 했을때
                    for dice in dices:
                        dice.status = 'stopped'
                    redrawGameWindow(dices)
                    if turn_cnt == 3:
                        turn_cnt = 0
                        state = 'player_turn'
