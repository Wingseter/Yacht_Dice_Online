from game.lib.core import(
    isEnd,
    Dicelist,
    Score,
    roll,
    turn,
    isValid,
    finishTurn,
)

from game.lib.gui import (
    pygame,
    drawBoard,
    drawButton,
    drawScore,
    drawDice,
    drawSave,
    diceAnimation,
    YACHT,
    Dice,
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

    return side, board, dice

def showScreen(win, side, board, player, score, dicelist, savelist, dices, saveDices):
    drawBoard(win)
    drawButton(win)
    drawScore(win, side, board, score)
    drawDice(win, dices, dicelist)
    drawSave(win, saveDices, savelist)
    pygame.display.update()