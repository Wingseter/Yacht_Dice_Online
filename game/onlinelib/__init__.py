from game.onlinelib.utils import *
from game.lib import *
from game.lib.utils import encode, decode
from game.lib.gui import Dice

def lobby(win, sock, key):
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
                    playerList = getPlayers(sock)
                    if playerList is None:
                        return
                    showLobby(win, key, playerList)
                    
                if 30 < x < 1100:
                    for i in range(len(playerList)):
                        if 172 + 30 * i < y < 208 + 30 * i:
                            write(sock, "rg" + playerList[i][:4])
                            newMsg = read()
                            if newMsg == "msgOk":
                                stat = request(win, None, sock)
                                if stat is None:
                                    return
                                elif stat and yacht(win, sock, 0):
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
                if request(win, msg[2:]):
                    write(sock, "gmOk" + msg[2:])
                    if yacht(win, sock, 1):
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
def yacht(win, sock, player):
    # 초기화
    side, board, dicelist, score, turn = initialize(win)
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

    while True:
        clock.tick(25)
        end = isEnd(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if end == True:
                    return
                if 900 < x < 1100 and 500 < y < 600:
                    if turn < 3:
                        score = roll(win, side, board, dicelist)
                        diceAnimation(win, dices, dicelist.lenDice())
                        turn = turn + 1
                        write(sock, encode("roll", dicelist.getDice()))
                if turn != 0:
                    if 310 < y < 400:
                        for i in range(dicelist.lenDice()):
                            width = 515 + 20 * i + 90 * i
                            if width  < x < width + 90:
                                dicelist.keep_dice(i)
                                write(sock, encode("keep", i))
                    if 140 < y < 206:
                        for j in range(5- dicelist.lenDice()):
                            width = 375 + 4 * j + 66 * j
                            if width < x < width + 66:
                                dicelist.disband_dice(j)
                                write(sock, encode("disb", j))
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
                                        sel = [i, j]
                    else:
                        sel = [-1, -1]

        showScreen(win, side, board, player, score, dicelist.giveDice(), dicelist.giveSave(), dices, saveDices, turn, total)
        
        if isValid(side, player, board, sel):
            side, board, score, sel, turn = finishTurn(side, board, score, dicelist, sel, turn)
            total = calcTotalScore(board)

        if readable():
            msg = read()
            if msg == "close":
                return True

            elif msg == "quit" or msg == "resign":
                write(sock, "end")
                return False

            elif side != player:
                action, data= decode(msg)

                if action == "roll":
                    score = onlineRoll(win, side, board, dicelist, data)
                    diceAnimation(win, dices, dicelist.lenDice())
                    turn = turn + 1
                elif action == "keep":
                    dicelist.keep_dice(data)
                elif action == "disb":
                    dicelist.disband_dice(data)
                elif action == "fins":
                    sel = [data/10 , data % 10]
                    if isValid(side, player, board, sel):
                        side, board, score, sel, turn = finishTurn(side, board, score, dicelist, sel, turn)
                        total = calcTotalScore(board)
                    else:
                        write(sock, "quit")
                        return True

        if side == player and isValid(side, player, board, sel):
            write(sock, encode("fins", i * 10 + j))
            side, board, score, sel, turn = finishTurn(side, board, score, dicelist, sel, turn)
            total = calcTotalScore(board)
