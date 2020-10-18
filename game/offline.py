
from game.lib import *

# offline 코드
def main(win, player):
    # 초기화
    side, board, dicelist = initialize(win)
    dicelist.drawDice(win)
    score = None
    clock = pygame.time.Clock()
    
    while True:
        clock.tick(25)
        end = isEnd(side)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 900 < x < 1100 and 500 < y < 600:
                    score = turn(win, side, board, dicelist)
                elif 310 < y < 400:
                    for i in range(dicelist.lenDice()):
                        width = 515 + 20 * i + 90 * i
                        if width  < x < width + 90:
                            dicelist.keep_dice(i)
            
        showScreen(win, side, board, player, dicelist, score)
        if side != player:
            if not end:
                sel = [0, 0]