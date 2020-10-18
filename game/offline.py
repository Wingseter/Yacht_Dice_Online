
from game.lib import *

# offline 코드
def main(win, player):
    # 초기화
    side, board, dicelist = initialize(win)
    dices = [
        Dice(465+50, 210+100, 90, 90),
        Dice(575+50, 210+100, 90, 90),
        Dice(685+50, 210+100, 90, 90),
        Dice(795+50, 210+100, 90, 90),
        Dice(905+50, 210+100, 90, 90)
    ]
    drawDice(win, dices, dicelist.giveAllDice())
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
                    score = play(win, side, board, dicelist)
                    diceAnimation(win, dices, dicelist.lenDice())
                elif 310 < y < 400:
                    for i in range(dicelist.lenDice()):
                        width = 515 + 20 * i + 90 * i
                        if width  < x < width + 90:
                            dicelist.keep_dice(i)
            
        showScreen(win, side, board, player, score, dicelist.giveDice(), dicelist.giveSave(), dices)
        if side != player:
            if not end:
                sel = [0, 0]