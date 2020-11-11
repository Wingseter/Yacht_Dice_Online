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


    return side, board, dice, score, turn

def showScreen(win, side, board, player, score, dicelist, savelist, dices, saveDices, turn, total, online, charactor, LOAD):
    drawBoard(win, charactor, LOAD)
    drawButton(win, turn, online)
    drawScore(win, side, board, score, total)
    drawDice(win, dices, dicelist, LOAD)
    drawSave(win, saveDices, savelist)
    drawEtc(win, side)
    pygame.display.update()