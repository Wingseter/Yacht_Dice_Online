import random

ACE = 1
DEUCES = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
BONUS_SCORE = 35
SSTRAIGHT_SCORE = 15
LSTRAIGHT_SCORE = 30
YACHT_SCORE = 50

def inEnd(side):
    return False


class Dice:
    def __init__(self):
        self.__saved = {}
        self.__dice = {"dice1" : 0, "dice2" : 0, "dice3" : 0, "dice4" : 0, "dice5" : 0}


    def roll_dice(self): # 각 라운드 처음과 나머지 구분, 처음에는 dice, save 구분
        for die in self.__dice:
            self.__dice[die] = random.randint(ACE, SIXES)
    

    def keep_dice(self, saveList): # 선택한 주사위의 값을 리스트로 받아서 처리
        if saveList == []:
            return
        for i in saveList:
            for key, value in self.__dice.items():
                if value == i:
                    self.__saved[key] = value
        for key in self.__saved.keys():
            del(self.__dice[key])
    

    def disband_dice(self, unsaveList): # saved -> dice
        if unsaveList == []:
            return
        for i in unsaveList:
            for key, value in self.__saved.items():
                if value == i:
                    self.__dice[key] = value
        for key in self.__dice.keys():
            del(self.__saved[key])
    

    def give_dice(self):
        all_dice = []
        if self.__saved == {}:
            for value in self.__dice.values():
                all_dice.append(value)
        else:
            for value in self.__saved:
                all_dice.append(value)
            for value in self.__dice:
                all_dice.append(value)
        return all_dice

    def print_saved(self):
        print("Saved =", self.__saved)
    

    def print_dice(self):
        print("Dice =", self.__dice)


class Turn: # 점수 판정 및 주사위 합쳐서 구성
    dc = Dice()


    def roll(self, onUp):
        # if onUp == TRUE:
        self.dc.roll_dice()

    
    # def set_turn(self):


class Score: # 점수 판정, 핸드 랭크
    __all_dice = []


    def __init__(self, all_dice):
        self.__all_dice = all_dice
        self.__all_dice.sort()


    def aces_score(self):
        a_score = 0
        for i in self.__all_dice:
            if i == ACE:
                a_score += ACE
        return a_score


    def deuces_score(self):
        d_score = 0
        for i in self.__all_dice:
            if i == DEUCES:
                d_score += DEUCES
        return d_score


    def threes_score(self):
        t_score = 0
        for i in self.__all_dice:
            if i == THREES:
                t_score += THREES
        return t_score


    def fours_score(self):
        f_score = 0
        for i in self.__all_dice:
            if i == FOURS:
                f_score += FOURS
        return f_score


    def fives_score(self):
        fv_score = 0
        for i in self.__all_dice:
            if i == FIVES:
                fv_score += FIVES
        return fv_score


    def sixes_score(self):
        s_score = 0
        for i in self.__all_dice:
            if i == SIXES:
                s_score += SIXES
        return s_score


    def sub_total_score(self):
        return (
            self.aces_score() + 
            self.deuces_score() + 
            self.threes_score() + 
            self.fours_score() +
            self.fives_score() +
            self.sixes_score() )


    def bonus_score(self):
        if self.sub_total_score() >= 63:
            return BONUS_SCORE
        else:
            return 0


    def choice_score(self):
        sum_of_all_dice = 0
        for i in self.__all_dice:
            sum_of_all_dice += i
        return sum_of_all_dice


    def four_of_a_kind_score(self):
        sum_of_all_dice = self.choice_score()
        
        if self.__all_dice[0] != self.__all_dice[1]:
            if self.__all_dice[1] != self.__all_dice[4]:
                return 0
            else:
                return sum_of_all_dice
        else:
            if self.__all_dice[0] != self.__all_dice[3]:
                return 0
            else:
                if self.__all_dice[3] == self.__all_dice[4]:
                    self.yacht_score()
                return sum_of_all_dice


    def fullhouse_score(self):
        sum_of_all_dice = self.choice_score()

        if self.__all_dice[0] == self.__all_dice[1]:
            if self.__all_dice[2] == self.__all_dice[4]:
                return sum_of_all_dice
            else:
                return 0
        elif self.__all_dice[0] == self.__all_dice[2]:
            if self.__all_dice[3] == self.__all_dice[4]:
                return sum_of_all_dice
            else:
                return 0
        return 0


    def sstraight_score(self):
        if self.__all_dice[0] == 1 and self.__all_dice[3] == 4:
            if self.__all_dice[1] != 3 and self.__all_dice[2] != 2:
                return SSTRAIGHT_SCORE
        if self.__all_dice[0] == 2 and self.__all_dice[3] == 5:
            if self.__all_dice[1] != 4 and self.__all_dice[2] != 3:
                return SSTRAIGHT_SCORE
        if self.__all_dice[1] == 2 and self.__all_dice[4] == 5:
            if self.__all_dice[2] != 4 and self.__all_dice[3] != 3:
                return SSTRAIGHT_SCORE
        if self.__all_dice[1] == 3 and self.__all_dice[4] == 6:
            if self.__all_dice[2] != 5 and self.__all_dice[3] != 4:
                return SSTRAIGHT_SCORE
        return 0


    def lstraight_score(self):
        if self.__all_dice is [1, 2, 3, 4, 5]:
            return LSTRAIGHT_SCORE
        if self.__all_dice is [2, 3, 4, 5, 6]:
            return LSTRAIGHT_SCORE
        return 0


    def yacht_score(self):
        for i in range(1, 7):
            if self.__all_dice[0] == i and self.__all_dice[4] == i:
                return YACHT_SCORE
        return 0


    def upper_section_score(self):
        return (self.sub_total_score() + self.bonus_score())


    def lower_section_score(self):
        return (
            self.choice_score() +
            self.four_of_a_kind_score() +
            self.fullhouse_score() +
            self.sstraight_score() +
            self.lstraight_score() +
            self.yacht_score())


    def total_score(self):
        return (self.upper_section_score() + self.lower_section_score())