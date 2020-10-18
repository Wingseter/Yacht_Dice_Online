from game.lib.core import(
    isEnd,
    Dicelist,
    Score,
    play,
    turn,
)

from game.lib.gui import (
    pygame,
    drawBoard,
    drawButton,
    drawScore,
    drawDice,
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

def showScreen(win, side, board, player, score, dicelist, savelist, dices):
    drawBoard(win)
    drawButton(win)
    drawScore(win, side, board, score)
    drawDice(win, dices, dicelist)
    pygame.display.update()