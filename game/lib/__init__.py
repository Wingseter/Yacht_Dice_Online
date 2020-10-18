from game.lib.core import(
    inEnd,
)

from game.lib.gui import (
    pygame,
    drawBoard,
    YACHT,
)

def showScreen(win):
    drawBoard(win)
    pygame.display.update()