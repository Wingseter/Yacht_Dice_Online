import pygame
from tools.utils import emptyRoundRect
from tools.textBox import textBox
import random
from loader import OFFLINEGAME
import time

state = 'player_turn'  # 누구의 턴인지 표시
turn_cnt = 0  # 총 3번 주사위를 굴릴 수 있다.
win = pygame.display.set_mode((1200, 750), 0, 32)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
myfont = pygame.font.SysFont('Comicsans', 30)


class Dice(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.side = 0
        self.status = 'stopped'
        self.tempx = x  # 주사위를 원위치 시키기 위한 변수
        self.tempy = y

    def roll(self, win):
        pygame.draw.rect(win, WHITE, (self.x, self.y, 100, 100))

        # 만약 멈춰 있는 상태라면 굴리는 상태로 변환
        if self.status == 'stopped':
            self.status = 'rolling'
        if self.status == 'finalroll':
            self.x = self.tempx
            self.y = self.tempy

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
        if self.status == 'rolling':
            self.x += random.randint(-5, 5)
            self.y += random.randint(-5, 5)


def showDices(dices):

    # 10번 굴리고 반환
    for i in range(0, 11):
        time.sleep(0.1)
        # 화면 업데이트 (총 10번 진행)
        emptyRoundRect(win, (0, 0, 0),
                       (35, 90, 590, 280), 4, 5)  # 주사위 굴리는 패널 부분만 업데이트
        for dice in dices:
            if i == 9:
                dice.status = 'finalroll'
            dice.roll(win)
            if i == 10:
                dice.status = 'stopped'

            mytext1 = myfont.render(str(dice.side), 1, WHITE)
            win.blit(mytext1, (dice.tempx, 120))
            mytext2 = myfont.render(str(dice.status), 1, WHITE)
            win.blit(mytext2, (dice.tempx, 140))
            mytext3 = myfont.render(str(state), 1, WHITE)
            win.blit(mytext3, (65, 170))
            pygame.display.update()

        if i == 10:
            return


def showProgress(win):
    win.fill((100, 111, 155))
    emptyRoundRect(win, (255, 255, 255), (25, 30, 1150, 700), 7, 5)  # 판
    emptyRoundRect(win, (255, 255, 255), (44, 390, 580, 320), 4, 5)  # 주사위 공간
    emptyRoundRect(win, (255, 255, 255), (40, 40, 100, 40), 7, 5)  # 기권
    emptyRoundRect(win, (255, 255, 255), (372, 40, 100, 40), 7, 5)  # 승리
    emptyRoundRect(win, (255, 255, 255), (650, 40, 510, 670), 7, 5)  # 족보 저장공간
    emptyRoundRect(win, (255, 255, 255), (650, 40, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 94, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 149, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 204, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 260, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 315, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 370, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 425, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 480, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 535, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 590, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 645, 510, 60), 7, 5)


def Winner(win, coordinate):
    clock = pygame.time.Clock()
    win_appearing = coordinate
    win.blit(OFFLINEGAME.WIN_APPEARING, win_appearing[:2])
    pygame.display.update()
    time.sleep(1)
    clock.tick(300)


def main(win):
    finish = False
    clock = pygame.time.Clock()
    global state
    global turn_cnt
    showProgress(win)

    red = pygame.color.Color('#FF0000')
    white = pygame.color.Color('#FFFFFF')
    black = pygame.color.Color('#000000')
    count = 0
    size = [500, 500]

    #승리, 기권
    winner = (408, 45, 70, 40)
    giveup = (55, 45, 70, 40)

    # 타이머
    counter, text = 10, '10'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)

    win.blit(OFFLINEGAME.GIVEUP, giveup[:2])
    win.blit(OFFLINEGAME.WINNER, winner[:2])

    # game loop(로직 생성)
    while not finish:
        dices = []
        clock.tick(60)
        # 주사위 객체들
        dices = [
            Dice(65, 210, 90, 90),
            Dice(175, 210, 90, 90),
            Dice(285, 210, 90, 90),
            Dice(395, 210, 90, 90),
            Dice(505, 210, 90, 90)
        ]
        # 주사위 굴리기
        for event in pygame.event.get():
            if state == 'player_turn':
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        turn_cnt += 1
                        # 마우스 클릭을 했을때
                        for dice in dices:
                            dice.status = 'stopped'
                        showDices(dices)
                        if turn_cnt == 3:
                            turn_cnt = 0
                            state = 'enemy_turn'
            elif state == "enemy_turn":
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        turn_cnt += 1
                        # 마우스 클릭을 했을때
                        for dice in dices:
                            dice.status = 'stopped'
                        showDices(dices)
                        if turn_cnt == 3:
                            turn_cnt = 0
                            state = 'player_turn'

            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:  # Give up 누르면 게임 종료
                x, y = event.pos
                if giveup[0] < x < sum(giveup[::2]) and giveup[1] < y < sum(giveup[1::2]):
                    finish = True
                elif winner[0] < x < sum(winner[::2]) and winner[1] < y < sum(winner[1::2]):
                    coordinate = (200, 100, 500, 500)
                    Winner(win, coordinate)
            elif event.type == pygame.QUIT:  # 파이 게임이 끝났으면
                finish = True

        # 기권

        # 타이머 counting
        for e in pygame.event.get(False):
            if e.type == pygame.USEREVENT:
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else 'boom!'
            if e.type == pygame.QUIT:
                break
        else:
            win.blit(font.render(text, True, (0, 0, 0)), (1000, 2, 30, 40))
            pygame.display.flip()
            clock.tick(60)
            continue
        break
