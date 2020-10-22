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

class Score: # 점수 판정, 핸드 랭크
    __all_dice = []


    def __init__(self, all_dice=None):
        if all_dice != None:
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




    def choice_score(self):
        sum_of_all_dice = 0
        for i in self.__all_dice:
            sum_of_all_dice += i
        return sum_of_all_dice


    def four_of_a_kind_score(self):
        kind = set(self.__all_dice)
        sum_of_all_dice = self.choice_score()
        for i in kind:
            count = 0
            for j in self.__all_dice:
                if i == j:
                    count += 1

            if count >= 4:
                return sum_of_all_dice

        return 0


    def fullhouse_score(self):
        kind = set(self.__all_dice)
        sum_of_all_dice = self.choice_score()
        count = [0 for _ in range(6)]

        for i in kind:
            for j in self.__all_dice:
                if i == j:
                    count[i-1] += 1

        if 3 in count and 2 in count:
            return sum_of_all_dice
        else:
            return 0
       


    def sstraight_score(self):
        count = 1
        for i in range(4):
            if self.__all_dice[i + 1] - self.__all_dice[i] == 1:
                count += 1

        if count >= 4:
            return SSTRAIGHT_SCORE
        else:
            return 0
        

    def lstraight_score(self):
        count = 1
        for i in range(4):
            if self.__all_dice[i + 1] - self.__all_dice[i] == 1:
                count += 1

        if count >= 5:
            return LSTRAIGHT_SCORE
        else:
            return 0
        

    def yacht_score(self):
        if len(set(self.__all_dice)) == 1:
            return YACHT_SCORE
        else:
            return 0

    def sub_total_score(self, board):
        return (
            board[0][0] + 
            board[1][0] + 
            board[2][0] + 
            board[3][0] +
            board[4][0] +
            board[5][0] )


    def bonus_score(self, board):
        if self.sub_total_score(board) >= 63:
            return BONUS_SCORE
        else:
            return 0

    def upper_section_score(self, board):
        return (self.sub_total_score(board) + self.bonus_score(board))


    def lower_section_score(self, board):
        return (
            board[6][0] + 
            board[7][0] + 
            board[8][0] + 
            board[9][0] +
            board[10][0])


    def total_score(self, board):
        return (self.upper_section_score(board) + self.lower_section_score(board))