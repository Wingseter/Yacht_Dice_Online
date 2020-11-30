from tools import sound
from game.lib import *
from game.onlinelib.utils import popup

# offline 코드
def main(win, player, LOAD):
    # 초기화
    side, board, dicelist, score, turn, total, sel, helpon, itemSelect = initialize(win)
    charactor = [LOAD[8], not LOAD[8]]
    dices = [
        Dice(465+50, 210+100, 100, 100, LOAD),
        Dice(575+50, 210+100, 100, 100, LOAD),
        Dice(685+50, 210+100, 100, 100, LOAD),
        Dice(795+50, 210+100, 100, 100, LOAD),
        Dice(905+50, 210+100, 100, 100, LOAD)
    ]
    saveDices = [
        Dice(375, 140, 66, 66, LOAD),
        Dice(445, 140, 66, 66, LOAD),
        Dice(515, 140, 66, 66, LOAD),
        Dice(585, 140, 66, 66, LOAD),
        Dice(655, 140, 66, 66, LOAD),
    ]
    drawDice(win, dices, dicelist.giveAllDice(), LOAD)
    clock = pygame.time.Clock()
    online = False
    item = [[2,2,2], [2,2,2]]
    oneMoreCounter = 0

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
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if 645 < y < 685:
                    if 595 < x < 695 :
                        itemSelect[2] = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # print(turn)
                # print(oneMoreCounter)
                if 1000< x < 1100 and 10 < y < 110:
                    if prompt(win):
                        return
                if 900 < x < 1100 and 500 < y < 600:
                    if turn < 3:
                        sound.play_roll(LOAD)
                        score = roll(win, side, board, dicelist, itemSelect)
                        diceAnimation(win, dices, dicelist.lenDice(), LOAD)
                        turn = turn + 1
                        item, itemSelect = useItem(side, item, itemSelect)
                if 645 < y < 685:
                    if turn < 3:
                        if 395 < x < 495 and item[side][0] > 0:
                            itemSelect[0] = not itemSelect[0]
                            if itemSelect[1] == True:
                                itemSelect[1] = False
                        if 495 < x < 595 and item[side][1] > 0:
                            itemSelect[1] = not itemSelect[1]
                            if itemSelect[0] == True:
                                itemSelect[0] = False
                    if 595 < x < 695 and item[side][2] > 0:
                        itemSelect[2] = True
                        turn = turn -1
                        oneMoreCounter += 1
                        item[side][2]  -= 1
                if 1130 < x < 1190 and 710 < y < 735:
                    sound.play_click(LOAD)
                    helpon = not helpon
                if turn + oneMoreCounter != 0:
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
                    else:
                        sel = [-1, -1]


        showScreen(win, side, board, player, score, dicelist.giveDice(), dicelist.giveSave(), dices, saveDices, turn, total, online, charactor, LOAD, helpon, itemSelect, item)
        if isValid(side, player, board, sel):
            side, board, score, sel, turn, itemSelect = finishTurn(side, board, score, dicelist, sel, turn, itemSelect)
            total = calcTotalScore(board)
            oneMoreCounter = 0