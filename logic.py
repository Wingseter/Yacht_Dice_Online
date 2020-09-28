def Count(dice, number):
    return len([y for y in dice if y == number])

def HighestRepeated(dice, minRepeats):
    unique = set(dice)
    repeats = [x for x in unique if Count(dice, x) >= minRepeats]
    return max(repeats) if repeats else 0

def OfAKind(dice, n):
    repeat_score = HighestRepeated(dice,n)
    remainder = [x for x in dice if x != repeat_score]
    return repeat_score * n + remainder

def SumOfSingle(dice, selected):
    return sum([x for x in dice if x == selected])

def Chance(dice):
    return sum(dice)

def FourOfAKind(dice):
    return OfAKind(dice, 4)

def SmallStraight(dice):
    return 15 if tuple(sorted(dice)) == (1,2,3,4,5) else 0

def LargeStraight(dice):
    return 30 if tuple(sorted(dice)) == (2,3,4,5,6) else 0

def full_house(dice):
    repeat_score = dice.Highestrepeated(dice, 3)
    if repeat_score > 0:
        rests = [x for x in dice if x != repeat_score]
        if len(set(rests)) == 1 and len(rests) == 2:
            return 25
        
    repeat_score = dice.Highestrepeated(dice, 2)
    if repeat_score > 0:
        rests = [x for x in dice if x != repeat_score]
        if len(set(rests)) == 1 and len(rests) == 3:
            return 25
    return 0

def Ones(dice):
    return SumOfSingle(dice,1)

def Twos(dice):
    return SumOfSingle(dice,2)

def Threes(dice):
    return SumOfSingle(dice,3)

def Fours(dice):
    return SumOfSingle(dice,4)

def Fives(dice):
    return SumOfSingle(dice,5)

def Sixes(dice):
    return SumOfSingle(dice,6)

def Yahtzee(dice):
    return 50 if len(dice) == 5 and len(set(dice)) == 1 else 0