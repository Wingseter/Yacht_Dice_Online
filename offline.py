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
state = 'player_turn'  # 누구의 턴인지 표시
turn_cnt = 0  # 총 3번 주사위를 굴릴 수 있다.

# win = pygame.display.set_mode((SC_WIDTH, SC_HEIGHT))
# pygame.display.set_caption('Yacht Dice Game')

# 족보계산
class Strategy():
    def __init__(self, strategies):
        self.strategies = strategies

    def set_dices(self, dices):
        self.dices = dices

    def calculate(self):
        self.sides = [dice.side for dice in self.dices]
        self.unique = set(self.sides)

        upper_score = 0
        for i in range(1, 7):
            if self.strategies['%ds' % i]['done']:
                continue

            score = self.sum_of_single(i)
            self.strategies['%ds' % i]['score'] = score
            upper_score += score

        if upper_score >= 63:
            self.strategies['Bonus']['score'] = 35

        if not self.strategies['Choice']['done']:
            self.strategies['Choice']['score'] = sum(self.sides)
        if not self.strategies['4-of-a-kind']['done']:
            self.strategies['4-of-a-kind']['score'] = self.of_a_kind(4)
        if not self.strategies['Full House']['done']:
            self.strategies['Full House']['score'] = self.full_house()
        if not self.strategies['S. Straight']['done']:
            self.strategies['S. Straight']['score'] = self.small_straight()
        if not self.strategies['L. Straight']['done']:
            self.strategies['L. Straight']['score'] = self.large_straight()
        if not self.strategies['Yacht']['done']:
            self.strategies['Yacht']['score'] = self.of_a_kind(5)

        self.strategies['Total']['score'] = 0
        for k, v in self.strategies.items():
            if v['done']:
                self.strategies['Total']['score'] += v['score']

        return self.strategies

    def count(self, number):
        return len([side for side in self.sides if side == number])

    def highest_repeated(self, min_repeats):
        repeats = [x for x in self.unique if self.count(x) >= min_repeats]
        return max(repeats) if repeats else 0

    def of_a_kind(self, n):
        hr = self.highest_repeated(n)

        if hr == 0:
            return 0

        if n == 5:
            return 50

        rests = [side for side in self.sides if side != hr]

        return hr * n + sum(rests)

    def sum_of_single(self, number):
        return sum([x for x in self.sides if x == number])

    def full_house(self):
        hr = self.highest_repeated(3)
        if hr > 0:
            rests = [side for side in self.sides if side != hr]
            if len(set(rests)) == 1 and len(rests) == 2:
                return 25

        hr = self.highest_repeated(2)
        if hr > 0:
            rests = [side for side in self.sides if side != hr]
            if len(set(rests)) == 1 and len(rests) == 3:
                return 25

        return 0

    def small_straight(self):
        if set([1, 2, 3, 4]).issubset(self.unique) or set([2, 3, 4, 5]).issubset(self.unique) or set(
                [3, 4, 5, 6]).issubset(self.unique):
            return 30
        return 0

    def large_straight(self):
        if set([1, 2, 3, 4, 5]).issubset(self.unique) or set([2, 3, 4, 5, 6]).issubset(self.unique):
            return 40
        return 0

#점수판 목록
strategies_order = ['1s', '2s', '3s', '4s', '5s', '6s', 'Bonus', 'Choice', '4-of-a-kind', 'Full House', 'S. Straight', 'L. Straight', 'Yacht', 'Total']
strategies = {
    '1s': 0,
    '2s': 0,
    '3s': 0,
    '4s': 0,
    '5s': 0,
    '6s': 0,
    'Bonus': 0,
    'Choice': 0,
    '4-of-a-kind': 0,
    'Full House': 0,
    'S. Straight': 0,
    'L. Straight': 0,
    'Yacht': 0,
    'Total': 0
}

# 족보 계산을 위한 점수판 초기화
strategy = Strategy(strategies)
for i, strategy_name in enumerate(strategies_order):
    strategies[strategy_name] = {
           'score': 0,
           'selected': False,
           'done': False
}

class Dice(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.side = 0
        self.status = 'stopped'
        self.tempx = x
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
            self.x += random.randint(-10, 10)
            self.y += random.randint(-10, 10)

    def getSide(self) :
        return self.side


def redrawGameWindow(dices):
    # 10번 굴리고 반환
    for i in range(0, 11):
        time.sleep(0.1)
        win.fill((100, 0, 0))
        emptyRoundRect(win, (255, 255, 255), (20, 100, 1150, 630), 14, 4)

        # 화면 업데이트 (총 10번 진행)
        for dice in dices:
            if i == 9:
                dice.status = 'finalroll'
            dice.roll(win)
            if i == 10:
                dice.status = 'stopped'

            mytext1 = myfont.render(str(dice.side), 1, BLACK)
            win.blit(mytext1, (dice.x + 20, 10))
            mytext2 = myfont.render(str(dice.status), 1, BLACK)
            win.blit(mytext2, (dice.x + 20, 30))
            mytext3 = myfont.render(str(state), 1, BLACK)
            win.blit(mytext3, (20, 10))


        # 점수 계산 및 점수판 출력
        strategy.set_dices(dices)
        strategy.calculate()
        for i, sName in enumerate(strategies_order) :
            score = strategies[sName]["score"]
            n_text = f"{sName:<20}"
            s_text = f"{score:>10}"
            nText = myfont.render(n_text, 1, WHITE)
            sText = myfont.render(s_text, 1, WHITE)
            win.blit(nText, (40, 30 * (i + 1) + 100))
            win.blit(sText, (180, 30 * (i + 1) + 100))    
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