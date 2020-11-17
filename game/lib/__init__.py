from game.lib.core import(
    isEnd,
    Dicelist,
    Score,
    roll,
    onlineRoll,
    isValid,
    finishTurn,
    calcTotalScore,
    whoIsWinner,
    useItem,
    setItemByChara,
)

from game.lib.gui import (
    pygame,
    drawBoard,
    drawButton,
    drawScore,
    drawDice,
    drawSave,
    diceAnimation,
    drawEtc,
    drawHelp,
    drawItem,
    YACHT,
    Dice,
    prompt,
)

def initialize(win):
    side = 0
    board = (
        [
            [0,-1],[0,-1],[0,-1],[0,-1],[0,-1],
            [0,-1],[0,-1],[0,-1],[0,-1],[0,-1],
            [0,-1],[0,-1]
        ],
        [
            [0,-1],[0,-1],[0,-1],[0,-1],[0,-1],
            [0,-1],[0,-1],[0,-1],[0,-1],[0,-1],
            [0,-1],[0,-1]
        ]
    )

    dice = Dicelist()

    score = None
    turn = 0
    total = [[0,0,0,0,0], [0,0,0,0,0]]
    sel = [-1,-1]
    helpon = False
    itemSelect = [False, False, False]

    return side, board, dice, score, turn, total, sel, helpon, itemSelect

def showScreen(win, side, board, player, score, dicelist, savelist, dices, saveDices, turn, total, online, charactor, LOAD, helpon, itemSelect, item):
    drawBoard(win, charactor, LOAD)
    drawButton(win, turn, online, LOAD)
    drawScore(win, side, board, LOAD, score, total)
    drawDice(win, dices, dicelist, LOAD)
    drawSave(win, saveDices, savelist, LOAD)
    drawEtc(win, side, LOAD)
    drawHelp(win, helpon)
    drawItem(win, side, item, itemSelect, LOAD)
    pygame.display.update()