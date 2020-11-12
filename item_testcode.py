#추후 offline.py에 합칠예정

dice_chance = 1 #한번 더 굴리기 찬스 횟수
n_select = 3 # 홀짝 가능 횟수
item_num = 0 # 기본 = 0, 홀수 = 1, 짝수 = 2 배정 번호


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
            item_num = 1
             if 900 < x < 1100 and 500 < y < 600:
                    if turn < 3:
                        sound.play_roll(LOAD)
                        score = roll(win, side, board, dicelist, item_num)
                        diceAnimation(win, dices, dicelist.lenDice())
                        turn = turn + 1
            n_select = n_select - 1
            item_num = 0
    
    #짝        
    elif 1000 < x < 1100 and 650 < y < 750:
        if n_select != 0:
            item_num = 2
            if 900 < x < 1100 and 500 < y < 600:
                    if turn < 3:
                        sound.play_roll(LOAD)
                        score = roll(win, side, board, dicelist, item_num)
                        diceAnimation(win, dices, dicelist.lenDice())
                        turn = turn + 1
            n_select = n_select - 1
            item_num = 0
               

# core.py
def roll(win, side, board, dicelist, item_num):
        dicelist.roll_dice(win, item_num)
        allDice = dicelist.giveAllDice()
        score = calculate_score(allDice, board)

def roll_dice(self, win, item_num): # 각 라운드 처음과 나머지 구분, 처음에는 dice, save 구분
    if item_num == 0:
        for i in range(len(self.__dice)):
            self.__dice[i] = random.randint(ACE, SIXES)
    elif item_num == 1:
        for i in range(len(self.__dice)):
            self.__dice[i] = random.randint(ACE, SIXES, 2)
    elif item_num == 2:
        for i in range(len(self.__dice)):
            self.__dice[i] = random.randint(DEUCES, SIXES, 2)