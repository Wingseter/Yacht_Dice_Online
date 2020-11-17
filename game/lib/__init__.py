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

def showScreen(win, side, board, player, score, dicelist, savelist, dices, saveDices, turn, total, online, n_select_side0, n_select_side1, dice_chance_side0, dice_chance_side1):
    drawBoard(win)
    drawButton(win, turn, online, side, n_select_side0, n_select_side1, dice_chance_side0, dice_chance_side1)
    drawScore(win, side, board, score, total)
    drawDice(win, dices, dicelist)
    drawSave(win, saveDices, savelist)
    drawEtc(win, side)
    pygame.display.update()