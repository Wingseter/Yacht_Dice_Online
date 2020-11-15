from tools import sound
from game.lib import *
from game.onlinelib.utils import popup

# offline 코드
def main(win, player, LOAD):
    # 초기화
    side, board, dicelist, score, turn = initialize(win)
    dice_chance = 1 #한번 더 굴리기 찬스 횟수
    n_select = 3 # 홀짝 가능 횟수
    item_num = 0 # 기본 = 0, 홀수 = 1, 짝수 = 2 배정 번호
    dices = [
        Dice(465+50, 210+100, 100, 100),
        Dice(575+50, 210+100, 100, 100),
        Dice(685+50, 210+100, 100, 100),
        Dice(795+50, 210+100, 100, 100),
        Dice(905+50, 210+100, 100, 100)
    ]
    saveDices = [
        Dice(375, 140, 66, 66),
        Dice(445, 140, 66, 66),
        Dice(515, 140, 66, 66),
        Dice(585, 140, 66, 66),
        Dice(655, 140, 66, 66),
    ]
    drawDice(win, dices, dicelist.giveAllDice())
    clock = pygame.time.Clock()
    total = [[0,0,0,0,0], [0,0,0,0,0]]
    sel = [-1,-1]
    online = False
    while True:
        clock.tick(25)
        end = isEnd(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if prompt(win):
                    return
            if end == True:
                    winner = whoIsWinner(total)
                    popup(win, "winner" + winner)
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 1000< x < 1100 and 10 < y < 110:
                    if prompt(win):
                        return
                if 900 < x < 1100 and 530 < y < 600:
                    if turn < 3:
                        sound.play_roll(LOAD)
                        score = roll(win, side, board, dicelist, item_num)
                        diceAnimation(win, dices, dicelist.lenDice())
                        turn = turn + 1
                # 한번 더 찬스
                if 900 < x < 1000 and 380 < y < 480:
                    if dice_chance != 0:
                        turn = turn -1
                        dice_chance = dice_chance - 1         
                #홀
                if 920 < x < 970 and 610 < y < 660:
                    if n_select != 0:
                        item_num = 1
                        if turn < 3:
                            sound.play_roll(LOAD)
                            score = roll(win, side, board, dicelist, item_num)
                            diceAnimation(win, dices, dicelist.lenDice())
                            turn = turn + 1
                        n_select = n_select - 1
                        item_num = 0                
                #짝        
                if 1000 < x < 1050 and 610 < y < 660:
                    if n_select != 0:
                        item_num = 2
                        if turn < 3:
                            sound.play_roll(LOAD)
                            score = roll(win, side, board, dicelist, item_num)
                            diceAnimation(win, dices, dicelist.lenDice())
                            turn = turn + 1
                        n_select = n_select - 1
                        item_num = 0
                if turn != 0:
                    if 310 < y < 400:
                        for i in range(dicelist.lenDice()):
                            width = 515 + 20 * i + 90 * i
                            if width  < x < width + 90:
                                sound.play_click(LOAD)
                                dicelist.keep_dice(i)
                    if 140 < y < 206:
                        for j in range(5- dicelist.lenDice()):
                            width = 375 + 4 * j + 66 * j
                            if width < x < width + 66:
                                sound.play_click(LOAD)
                                dicelist.disband_dice(j)
                    if 155 < x < 370:
                        for i in range(len(board)):
                            width = 155 + 100 * i
                            height = 0
                            if width < x < width + 100:
                                for j in range(len(board[i])):
                                    # Upper
                                    if j < 6:
                                        height = 100 + 40 * j
                                    # Choice
                                    elif j == 6: 
                                        height = 405
                                    # Lower
                                    else:
                                        height = 450 + 40 * (j - 7)

                                    if height < y < height + 40:
                                        sound.play_select(LOAD)
                                        sel = [i, j]
                                        print(sel)
                    else:
                        sel = [-1, -1]

        showScreen(win, side, board, player, score, dicelist.giveDice(), dicelist.giveSave(), dices, saveDices, turn, total, online, dice_chance, n_select)
        if isValid(side, player, board, sel):
            side, board, score, sel, turn = finishTurn(side, board, score, dicelist, sel, turn)
            total = calcTotalScore(board)