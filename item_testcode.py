#추후 offline.py에 합칠예정

dice_chance = 1 #한번 더 굴리기 찬스 횟수
n_select = 3 # 홀짝 가능 횟수

if event.type == pygame.MOUSEBUTTONDOWN:
    x,y event.pos
    # 한번 더 찬스
    if 900 < x < 1000 and 380 < y < 480:
        if dice_chance != 0:
            turn = turn -1
            dice_chance = dice_chance - 1
    #홀
    if 880 < x < 980 and 650 < y < 750:
        if n_select != 0:

             if 900 < x < 1100 and 500 < y < 600:
                    if turn < 3:
                        sound.play_roll(LOAD)
                        score = odd_roll(win, side, board, dicelist)
                        diceAnimation(win, dices, dicelist.lenDice())
                        turn = turn + 1

            n_select = n_select - 1
    #짝        
    elif 1000 < x < 1100 and 650 < y < 750:
        if n_select != 0:

             if 900 < x < 1100 and 500 < y < 600:
                    if turn < 3:
                        sound.play_roll(LOAD)
                        score = even_roll(win, side, board, dicelist)
                        diceAnimation(win, dices, dicelist.lenDice())
                        turn = turn + 1

            n_select = n_select - 1
               

# core.py
def odd_roll(win, side, board, dicelist):
    dicelist.odd_roll_dice(win)
    allDice = dicelist.giveAllDice()
    score = calculate_score(allDice, board)

def odd_roll_dice(self, win):
    for i in range(len(self.__dice)):
        self.__dice[i] = random.randint(ACE, SIXES, 2)

    return score

def even_roll(win, side, board, dicelist):
    dicelist.even_roll_dice(win)
    allDice = dicelist.giveAllDice()
    score = calculate_score(allDice, board)

def even_roll_dice(self, win):
    for i in range(len(self.__dice)):
        self.__dice[i] = random.randint(TWOS, SIXES, 2)

    return score
