import random
import pygame
from tools.utils import emptyRoundRect
from game.lib.score import *

# 게임 끝났는지 판별
def isEnd(board):
    for player in board:
        for done in player:
            if done[1] == -1:
                return False
    return True

# 턴 전환
def flip(side):
    return int(not side)

def calculate_score(allDice, board):
    cal = Score(allDice)                            
    ONES = cal.aces_score()                         #0
    TWOS = cal.deuces_score()                       #1
    THREES = cal.threes_score()                     #2
    FOURS = cal.fours_score()                       #3
    FIVES = cal.fives_score()                       #4
    SIXES = cal.sixes_score()                       #5
    CHOICE = cal.choice_score()                     #6
    FOUR_OF_A_KIND = cal.four_of_a_kind_score()     #7
    FULL_HOUSE = cal.fullhouse_score()              #8
    SMALL_STRAIGHT = cal.sstraight_score()          #9
    LARGE_STRAIGHT = cal.lstraight_score()          #10
    YACHT = cal.yacht_score()

    copy = [ONES, TWOS, THREES, FOURS, FIVES, SIXES,  CHOICE,
     FOUR_OF_A_KIND, FULL_HOUSE, SMALL_STRAIGHT, LARGE_STRAIGHT, YACHT
    ]
    return copy

def calcTotalScore(board):
    cal = Score()
    total = list()
    for i in range(2):
        SUB_TOTAL_SCORE = cal.sub_total_score(board[i])
        BONUS_SCORE = cal.bonus_score(board[i])
        UPPER = SUB_TOTAL_SCORE + BONUS_SCORE
        LOWER = cal.lower_section_score(board[i])
        TOTAL = UPPER + LOWER

        total.append([SUB_TOTAL_SCORE, BONUS_SCORE, UPPER, LOWER, TOTAL])
    return total

def roll(win, side, board, dicelist):
    dicelist.roll_dice(win)
    allDice = dicelist.giveAllDice()
    score = calculate_score(allDice, board)

    return score

def turn():
    pass

def isValid(side, player, board, sel):
    if sel[0] != side:
        return False
    if sel[0] == -1 or sel[1] == -1:
        return False
    if board[sel[0]][sel[1]][1] == -1:
        return True
    return False

def finishTurn(side, board, score, dicelist, sel, turn):
    newSide = flip(side)
    board[sel[0]][sel[1]][0] = score[sel[1]]
    board[sel[0]][sel[1]][1] = 1
    newBoard = board
    newScore = None
    newSel = [-1, -1]
    dicelist.reset()
    newTurn = 0
    return newSide, newBoard, newScore, newSel, newTurn


class Dicelist:
    def __init__(self):
        self.__saved = []
        self.__dice = [0,0,0,0,0]
        for i in range(len(self.__dice)):
            self.__dice[i] = random.randint(ACE, SIXES)

    def reset(self):
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
    

    def disband_dice(self, unsave): # saved -> dice
        if unsave == None:
            return
        self.__dice.append(self.__saved.pop(unsave))
    

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

   



