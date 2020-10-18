import random
import pygame
import time 
from tools.utils import emptyRoundRect
from loader import WHITE, BLACK
from game.lib.gui import drawScore
from game.lib.score import *

# 게임 끝났는지 판별
def isEnd(side):
    return False

# 턴 전환
def flip(side):
    return int(not side)

def calculate_score(allDice):
    cal = Score(allDice)
    ONES = cal.aces_score()
    TWOS = cal.deuces_score()
    THREES = cal.threes_score()
    FOURS = cal.fours_score()
    FIVES = cal.fives_score()
    SIXES = cal.sixes_score()
    SUB_TOTAL_SCORE = cal.sub_total_score()
    BONUS_SCORE = cal.bonus_score()
    CHOICE = cal.choice_score()
    FOUR_OF_A_KIND = cal.four_of_a_kind_score()
    FULL_HOUSE = cal.fullhouse_score()
    SMALL_STRAIGHT = cal.sstraight_score()
    LARGE_STRAIGHT = cal.lstraight_score()
    YACHT = cal.yacht_score()
    UPPER = cal.upper_section_score()
    LOWER = cal.lower_section_score()
    TOTAL = cal.total_score()

    copy = [ONES, TWOS, THREES, FOURS, FIVES, SIXES,  CHOICE,
     FOUR_OF_A_KIND, FULL_HOUSE, SMALL_STRAIGHT, LARGE_STRAIGHT, YACHT,
     SUB_TOTAL_SCORE, BONUS_SCORE, UPPER, LOWER, TOTAL]
    return copy

def turn(win, side, board, dicelist):
    dicelist.roll_dice(win)
    allDice = dicelist.give_dice()
    score = calculate_score(allDice)
    return score

class Dicelist:
    def __init__(self, allDice):
        self.__saved = []
        self.__dice = [0,0,0,0,0]
        for i in range(len(self.__dice)):
            self.__dice[i] = random.randint(ACE, SIXES)
        self.dices = allDice

    def lenDice(self):
        return len(self.__dice)

    def roll_dice(self, win): # 각 라운드 처음과 나머지 구분, 처음에는 dice, save 구분
        for i in range(len(self.__dice)):
            self.__dice[i] = random.randint(ACE, SIXES)
        self.diceAnimation(win)
        pygame.draw.rect(win, (100, 200, 200), (465, 260, 635, 200)) # 주사위 굴리는 패널 부분만 업데이트
        self.drawDice(win)
        print(self.__dice)
    

    def keep_dice(self, save): # 선택한 주사위의 값을 리스트로 받아서 처리
        if save == None:
            return
        self.__saved.append(self.__dice.pop(save))
    

    def disband_dice(self, unsaveList): # saved -> dice
        if unsaveList == None:
            return
        self.__dice.append(self.__saved)
    

    def give_dice(self):
        all_dice = []
        if self.__saved == []:
            for value in self.__dice:
                all_dice.append(value)
        else:
            for value in self.__saved:
                all_dice.append(value)
            for value in self.__dice:
                all_dice.append(value)
        return all_dice

    def drawDice(self, win):
        for dice, side in zip(self.dices, self.__dice):
            dice.draw(win, side)
    
    def diceAnimation(self, win):
        for i in range(0, 11):
            time.sleep(0.1)
            pygame.draw.rect(win, (100, 200, 200), (465, 260, 635, 200)) # 주사위 굴리는 패널 부분만 업데이트
            for dice in self.dices:
                if i == 9:
                    dice.status = 'finalroll'
                dice.roll(win)
                if i == 10:
                    dice.status = 'stopped'

                pygame.display.update()



class Dice:
    def __init__(self, x= 0, y=0, width= 0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.side = 0
        self.status = 'stopped'
        self.tempx = x  # 주사위를 원위치 시키기 위한 변수
        self.tempy = y

    # 주사위 눈에 따른 모습 변화
    def draw(self, win, side):
        pygame.draw.rect(win, WHITE, (self.x, self.y, 100, 100))

        # 만약 멈춰 있는 상태라면 굴리는 상태로 변환
        if self.status == 'stopped':
            self.status = 'rolling'
        # 마지막으로 구르고나서 제자리로 돌아감
        if self.status == 'finalroll':
            self.x = self.tempx
            self.y = self.tempy

        if side == 1 or side == 3 or side == 5:
            pygame.draw.circle(win, BLACK, (self.x + 50, self.y + 50), 8, 8)
        if side == 4 or side == 5 or side == 6:
            pygame.draw.circle(win, BLACK, (self.x + 20, self.y + 20), 8, 8)
        if side == 6:
            pygame.draw.circle(win, BLACK, (self.x + 20, self.y + 50), 8, 8)
        if side == 2 or side == 3 or side == 4 or side == 5 or side == 6:
            pygame.draw.circle(win, BLACK, (self.x + 20, self.y + 80), 8, 8)
        if side == 2 or side == 3 or side == 4 or side == 5 or side == 6:
            pygame.draw.circle(win, BLACK, (self.x + 80, self.y + 20), 8, 8)
        if side == 6:
            pygame.draw.circle(win, BLACK, (self.x + 80, self.y + 50), 8, 8)
        if side == 4 or side == 5 or side == 6:
            pygame.draw.circle(win, BLACK, (self.x + 80, self.y + 80), 8, 8)

    # 주사위 굴리기
    def roll(self, win):
        self.side = random.randint(1, 6)
        self.draw(win, self.side)

       # 주사위 애니메이션
        if self.status == 'rolling':
            self.x += random.randint(-4, 4)
            self.y += random.randint(-4, 4)

