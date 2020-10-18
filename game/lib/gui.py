import pygame
from loader import YACHT, putNum, putGreyNum, WHITE

def drawBoard(win):
    win.fill((100, 200, 200))
    # updown grid
    pygame.draw.line(win, WHITE, [5, 125], [10, 125], 2)
    pygame.draw.line(win, WHITE, [360, 125], [1275, 125], 2)
    
    # board
    pygame.draw.rect(win, WHITE, [370, 135, 900, 575], 2)
    
    # keep disband
    pygame.draw.rect(win, WHITE, [375, 140, 66, 66], 1)
    pygame.draw.rect(win, WHITE, [445, 140, 66, 66], 1)
    pygame.draw.rect(win, WHITE, [515, 140, 66, 66], 1)
    pygame.draw.rect(win, WHITE, [585, 140, 66, 66], 1)
    pygame.draw.rect(win, WHITE, [655, 140, 66, 66], 1)
    
    # score board
    pygame.draw.rect(win, WHITE, [10, 10, 350, 700], 2)
    
    # player
    pygame.draw.rect(win, WHITE, [155, 40, 200, 60], 2)
    pygame.draw.line(win, WHITE, [255, 40], [255, 100], 2)
    win.blit(YACHT.text_com, [270, 55])
    win.blit(YACHT.text_player, [192, 55])
    
    # upper section
    pygame.draw.rect(win, WHITE, [15, 100, 340, 300], 2)
    pygame.draw.line(win, WHITE, [15, 140], [355, 140], 2)
    pygame.draw.line(win, WHITE, [15, 180], [355, 180], 2)
    pygame.draw.line(win, WHITE, [15, 220], [355, 220], 2)
    pygame.draw.line(win, WHITE, [15, 260], [355, 260], 2)
    pygame.draw.line(win, WHITE, [15, 300], [355, 300], 2)
    pygame.draw.line(win, WHITE, [15, 340], [355, 340], 2)
    pygame.draw.line(win, WHITE, [155, 365], [355, 365], 1)
    pygame.draw.line(win, WHITE, [155, 100], [155, 400], 4)
    pygame.draw.line(win, WHITE, [255, 100], [255, 400], 1)
    win.blit(YACHT.dice_ace32, [20, 105])
    win.blit(YACHT.dice_deuces32, [20, 145])
    win.blit(YACHT.dice_threes32, [20, 185])
    win.blit(YACHT.dice_fours32, [20, 225])
    win.blit(YACHT.dice_fives32, [20, 265])
    win.blit(YACHT.dice_sixes32, [20, 305])
    win.blit(YACHT.text_ace, [65, 112])
    win.blit(YACHT.text_deuces, [65, 152])
    win.blit(YACHT.text_threes, [65, 192])
    win.blit(YACHT.text_fours, [65, 232])
    win.blit(YACHT.text_fives, [65, 272])
    win.blit(YACHT.text_sixes, [65, 312])
    win.blit(YACHT.text_subtotal, [34, 360])
    
    # choice score
    pygame.draw.rect(win,WHITE, [15, 405, 340, 40], 2)
    pygame.draw.line(win, WHITE, [155, 405], [155, 445], 4)
    pygame.draw.line(win, WHITE, [255, 405], [255, 445], 1)
    win.blit(YACHT.choice32, [20, 410])
    win.blit(YACHT.text_choice, [65, 415])
    
    # lower section
    pygame.draw.rect(win, WHITE, [15, 450, 340, 200], 2)
    pygame.draw.line(win, WHITE, [15, 490], [355, 490], 2)
    pygame.draw.line(win, WHITE, [15, 530], [355, 530], 2)
    pygame.draw.line(win, WHITE, [15, 570], [355, 570], 2)
    pygame.draw.line(win, WHITE, [15, 610], [355, 610], 2)
    pygame.draw.line(win, WHITE, [155, 450], [155, 650], 4)
    pygame.draw.line(win, WHITE, [255, 450], [255, 650], 1)
    win.blit(YACHT.fourofakind32, [20, 455])
    win.blit(YACHT.fullhouse32, [20, 495])
    win.blit(YACHT.sstraight32, [20, 535])
    win.blit(YACHT.lstraight32, [20, 575])
    win.blit(YACHT.yacht32, [20, 615])
    win.blit(YACHT.text_fourofakind, [65, 460])
    win.blit(YACHT.text_fullhouse, [65, 500])
    win.blit(YACHT.text_sstraight, [65, 540])
    win.blit(YACHT.text_lstraight, [65, 580])
    win.blit(YACHT.text_yacht, [65, 620])
    
    # total
    pygame.draw.rect(win, WHITE, [15, 655, 340, 50], 2)
    pygame.draw.line(win, WHITE, [155, 655], [155, 705], 4)
    pygame.draw.line(win, WHITE, [255, 655], [255, 705], 1)
    win.blit(YACHT.text_total, [53, 670])

def drawScore(win, side, board, newScore=None):
    for i, eachPlayer in enumerate(board):
        for j, oldScore in enumerate(eachPlayer):
            if oldScore[1] != -1:
                putNum(win, oldScore[0], (100 + 100 * i, 100 + 100* j))
            else:
                if newScore != None and side == i:
                    putGreyNum(win, newScore[j], (200 + 100 * i, 100 + 40* j))

def drawButton(win):
    win.blit(YACHT.ROLL, [900, 500])
