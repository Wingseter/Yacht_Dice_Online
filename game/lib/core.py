import random
import pygame
from tools.utils import emptyRoundRect
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

def play(win, side, board, dicelist):
    dicelist.roll_dice(win)
    allDice = dicelist.giveAllDice()
    score = calculate_score(allDice)
    return score

def turn():
    pass

class Dicelist:
    def __init__(self):
        self.__saved = []
        self.__dice = [0,0,0,0,0]
        for i in range(len(self.__dice)):
            self.__dice[i] = random.randint(ACE, SIXES)

    def lenDice(self):
        return len(self.__dice)

    def roll_dice(self, win): # 각 라운드 처음과 나머지 구분, 처음에는 dice, save 구분
        for i in range(len(self.__dice)):
            self.__dice[i] = random.randint(ACE, SIXES)

    def keep_dice(self, save): # 선택한 주사위의 값을 리스트로 받아서 처리
        if save == None:
            return
        self.__saved.append(self.__dice.pop(save))
    

    def disband_dice(self, unsaveList): # saved -> dice
        if unsaveList == None:
            return
        self.__dice.append(self.__saved)
    

    def giveAllDice(self):
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

    def giveDice(self):
        all_dice = []
        for value in self.__dice:
            all_dice.append(value)
        return all_dice

    def giveSave(self):
        all_dice = []
        for value in self.__saved:
            all_dice.append(value)
        return all_dice

   



