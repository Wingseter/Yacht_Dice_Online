from game.lib.core import(
    isEnd,
    Dicelist,
    Score,
    Dice,
    turn
)

from game.lib.gui import (
    pygame,
    drawBoard,
    drawButton,
    drawScore,
    YACHT,
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

    dices = [
        Dice(465+50, 210+100, 90, 90),
        Dice(575+50, 210+100, 90, 90),
        Dice(685+50, 210+100, 90, 90),
        Dice(795+50, 210+100, 90, 90),
        Dice(905+50, 210+100, 90, 90)
    ]
    dice = Dicelist(dices)

    return side, board, dice

def showScreen(win, side, board, player, dicelist, score):
    drawBoard(win)
    drawButton(win)
    drawScore(win, side, board, score)
    dicelist.drawDice(win)
    pygame.display.update()