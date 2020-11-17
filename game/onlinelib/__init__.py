from game.onlinelib.utils import *
from game.lib import *
from game.lib.utils import encode, decode, truefalse
from game.lib.gui import Dice
from tools import sound
import time

def lobby(win, sock, key, LOAD):
    clock = pygame.time.Clock()

    playerList = getPlayers(sock)
    if playerList is None:
        return
    showLobby(win, key, playerList)

    while True:
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame. QUIT:
                write(sock, "quit")
                return
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # 새로고침 했을때
                if 450 < x < 480 and 120 < y < 150:
                    sound.play_click(LOAD)
                    playerList = getPlayers(sock)
                    if playerList is None:
                        return
                    showLobby(win, key, playerList)
                    
                if 30 < x < 1100:
                    for i in range(len(playerList)):
                        if 172 + 30 * i < y < 208 + 30 * i:
                            sound.play_click(LOAD)
                            write(sock, "rg" + playerList[i][:4])
                            newMsg = read()
                            if newMsg == "msgOk":
                                charactor = [int(playerList[i][-2]), LOAD[8]]
                                stat = request(win, None, LOAD, sock)
                                if stat is None:
                                    return
                                elif stat and yacht(win, sock, 1, LOAD, charactor):
                                    return

                            playerList = getPlayers(sock)
                            if playerList is None:
                                return
                            showLobby(win, key, playerList)
                            
        if readable():
            msg = read()
            
            if msg == "close":
                return

            elif msg.startswith("gr"):
                if request(win, msg[2:], LOAD):
                    write(sock, "gmOk" + msg[2:-1])
                    charactor = [LOAD[8], truefalse(int(msg[-1]))]
                    if yacht(win, sock, 0, LOAD, charactor):
                        return
                    else:
                        playerList = getPlayers(sock)
                        if playerList is None:
                            return
                        showLobby(win, key, playerList)
                else:
                    write(sock, "gmNo" + msg[2:])
                    showLobby(win, key, playerList)



# offline 코드
def yacht(win, sock, player, LOAD, charactor):
    # 초기화
    side, board, dicelist, score, turn = initialize(win)

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
    total = [[0,0,0,0,0], [0,0,0,0,0]]
    sel = [-1,-1]
    online = True

    while True:
        clock.tick(25)
        end = isEnd(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if prompt(win):
                    write(sock, "quit")
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if end == True:
                    winner = whoIsWinner(total)
                    if int(winner) == player +1:
                        popup(win, "win")
                        write(sock, "win")  
                    else:
                        popup(win, "lose")
                        write(sock, "lose") 
                    return False
                else:
                    if 750 < x < 850 and 10 < y < 110:
                        write(sock, "resign")
                        return False

                if side == player:
                    if 900 < x < 1100 and 500 < y < 600:
                        if turn < 3:
                            sound.play_roll(LOAD)
                            score = roll(win, side, board, dicelist)
                            write(sock, encode("rol", dicelist.getDice()))
                            diceAnimation(win, dices, dicelist.lenDice(), LOAD)
                            turn = turn + 1
                    if turn != 0:
                        if 310 < y < 400:
                            for i in range(dicelist.lenDice()):
                                width = 515 + 20 * i + 90 * i
                                if width  < x < width + 90:
                                    sound.play_click(LOAD)
                                    dicelist.keep_dice(i)
                                    write(sock, encode("kep", [i]))
                        if 140 < y < 206:
                            for j in range(5- dicelist.lenDice()):
                                width = 375 + 4 * j + 66 * j
                                if width < x < width + 66:
                                    sound.play_click(LOAD)
                                    dicelist.disband_dice(j)
                                    write(sock, encode("dis", [j]))
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
                            

        showScreen(win, side, board, player, score, dicelist.giveDice(), dicelist.giveSave(), dices, saveDices, turn, total, online, charactor, LOAD)

        if readable():
            msg = read()
            if msg == "close":
                return False

            elif msg == "quit":
                popup(win, msg)
                write(sock, "end")
                return False
            elif msg == "resign":
                popup(win, msg)
                write(sock, "win")
                return False
            elif side != player:
                action, data= decode(msg)

                if action == "rol":
                    score = onlineRoll(win, side, board, dicelist, data)
                    diceAnimation(win, dices, dicelist.lenDice(), LOAD)
                    turn = turn + 1
                elif action == "kep":
                    dicelist.keep_dice(int(data))
                elif action == "dis":
                    dicelist.disband_dice(int(data))
                elif action == "fin":
                    sel = [int(data[:1]) , int(data[1:])]
                    if isValid(side, player, board, sel):
                        side, board, score, sel, turn = finishTurn(side, board, score, dicelist, sel, turn,)
                        total = calcTotalScore(board)
                        sel = [-1, -1]
                    else:
                        write(sock, "quit")
                        return True

        if side == player and isValid(side, player, board, sel):
            write(sock, encode("fin", sel))
            side, board, score, sel, turn = finishTurn(side, board, score, dicelist, sel, turn)
            total = calcTotalScore(board)
