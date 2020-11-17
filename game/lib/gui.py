import pygame
import random
import time 
import menus.pref
from loader import YACHT, HELP, putNum, putLargeNum, putGreyNum, WHITE, RED, BLACK, BLUE, BG_WOOD, BG_GREEN, BG_BLACK, BG_SKY
from tools.utils import emptyRoundRect

class Dice:
    def __init__(self, x, y, width, height, LOAD):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.side = 0
        self.status = 'stopped'
        self.tempx = x  # 주사위를 원위치 시키기 위한 변수
        self.tempy = y
        if LOAD[5] == True:
            self.diceColor = WHITE
            self.diceDot = BLACK
        elif LOAD[6] == True:
            self.diceColor = RED
            self.diceDot = WHITE
        elif LOAD[7] == True:
            self.diceColor = BLUE
            self.diceDot = WHITE

    # 주사위 눈에 따른 모습 변화
    def draw(self, win, side, LOAD):
        pygame.draw.rect(win, self.diceColor, (self.x, self.y, self.width, self.height))

        # 만약 멈춰 있는 상태라면 굴리는 상태로 변환
        if self.status == 'stopped':
            self.status = 'rolling'
        # 마지막으로 구르고나서 제자리로 돌아감
        if self.status == 'finalroll':
            self.x = self.tempx
            self.y = self.tempy

        if side == 1 or side == 3 or side == 5:
            pygame.draw.circle(win, self.diceDot, (self.x + int(self.width/2)  , self.y + int(self.height/2)), 8, 8)
        if side == 4 or side == 5 or side == 6:
            pygame.draw.circle(win, self.diceDot, (self.x + int(self.width/5)  , self.y + int(self.height/5)), 8, 8)
        if side == 6:
            pygame.draw.circle(win, self.diceDot, (self.x + int(self.width/5)  , self.y + int(self.height/2)), 8, 8)
        if side == 2 or side == 3 or side == 4 or side == 5 or side == 6:
            pygame.draw.circle(win, self.diceDot, (self.x + int(self.width/5)  , self.y + int(self.height*4/5)), 8, 8)
        if side == 2 or side == 3 or side == 4 or side == 5 or side == 6:
            pygame.draw.circle(win, self.diceDot, (self.x + int(self.width*4/5), self.y + int(self.height/5)), 8, 8)
        if side == 6:
            pygame.draw.circle(win, self.diceDot, (self.x + int(self.width*4/5), self.y + int(self.height/2)), 8, 8)
        if side == 4 or side == 5 or side == 6:
            pygame.draw.circle(win, self.diceDot, (self.x + int(self.width*4/5), self.y + int(self.height*4/5)), 8, 8)

    # 주사위 굴리기
    def roll(self, win, LOAD):
        self.side = random.randint(1, 6)
        self.draw(win, self.side, LOAD)

       # 주사위 애니메이션
        if self.status == 'rolling':
            self.x += random.randint(-4, 4)
            self.y += random.randint(-4, 4)

# 설정에 따른 백그라운드 변경
def checkBackground(LOAD):
    BG_COLOR = (255, 255, 255)
    if LOAD[1] == True:
        BG_COLOR = BG_WOOD
    elif LOAD[2] == True:
        BG_COLOR = BG_GREEN
    elif LOAD[3] == True:
        BG_COLOR = BG_BLACK
    elif LOAD[4] == True:
        BG_COLOR = BG_SKY
    return BG_COLOR

def drawDice(win, dices, eyes, LOAD):
    for dice, eye in zip(dices, eyes):
        dice.draw(win, eye, LOAD)

def drawSave(win, dices, eyes, LOAD):
    for dice, eye in zip(dices, eyes):
        dice.draw(win, eye, LOAD)

def diceAnimation(win, dices, lenDice, LOAD):
    for i in range(0, 11):
        time.sleep(0.1)
        pygame.draw.rect(win,checkBackground(LOAD), (465, 260, 635, 200)) # 주사위 굴리는 패널 부분만 업데이트
        for j in range(lenDice):
            if i == 9:
                dices[j].status = 'finalroll'
            dices[j].roll(win, LOAD)
            if i == 10:
                dices[j].status = 'stopped'

            pygame.display.update()

def drawBoard(win, charactor, LOAD):
    win.fill(checkBackground(LOAD))
    BOARDCOLOR = WHITE
    if LOAD[9] == False:
        BOARDCOLOR = BLACK
    elif LOAD[9] == True:
        BOARDCOLOR == WHITE
    # updown grid
    pygame.draw.line(win, BOARDCOLOR, [5, 125], [10, 125], 2)
    pygame.draw.line(win, BOARDCOLOR, [360, 125], [1275, 125], 2)
    
    # board
    pygame.draw.rect(win, BOARDCOLOR, [370, 135, 900, 575], 2)
    
    # keep disband
    pygame.draw.rect(win, BOARDCOLOR, [375, 140, 66, 66], 1)
    pygame.draw.rect(win, BOARDCOLOR, [445, 140, 66, 66], 1)
    pygame.draw.rect(win, BOARDCOLOR, [515, 140, 66, 66], 1)
    pygame.draw.rect(win, BOARDCOLOR, [585, 140, 66, 66], 1)
    pygame.draw.rect(win, BOARDCOLOR, [655, 140, 66, 66], 1)
    
    # score board
    pygame.draw.rect(win, BOARDCOLOR, [10, 10, 350, 700], 2)
    
    # player
    pygame.draw.rect(win, BOARDCOLOR, [155, 40, 200, 60], 2)
    pygame.draw.line(win, BOARDCOLOR, [255, 40], [255, 100], 2)

    for i, chara in enumerate(charactor):
        x = 192 + (i * 95) 
        if chara == True:
            win.blit(YACHT.MINILISA, [x, 50])
        else:
            win.blit(YACHT.MINIBABEL, [x, 50])
    
    # upper section
    pygame.draw.rect(win, BOARDCOLOR, [15, 100, 340, 300], 2)
    pygame.draw.line(win, BOARDCOLOR, [15, 140], [355, 140], 2)
    pygame.draw.line(win, BOARDCOLOR, [15, 180], [355, 180], 2)
    pygame.draw.line(win, BOARDCOLOR, [15, 220], [355, 220], 2)
    pygame.draw.line(win, BOARDCOLOR, [15, 260], [355, 260], 2)
    pygame.draw.line(win, BOARDCOLOR, [15, 300], [355, 300], 2)
    pygame.draw.line(win, BOARDCOLOR, [15, 340], [355, 340], 2)
    pygame.draw.line(win, BOARDCOLOR, [155, 365], [355, 365], 1)
    pygame.draw.line(win, BOARDCOLOR, [155, 100], [155, 400], 4)
    pygame.draw.line(win, BOARDCOLOR, [255, 100], [255, 400], 1)
    win.blit(YACHT.dice_ace32, [20, 105])
    win.blit(YACHT.dice_deuces32, [20, 145])
    win.blit(YACHT.dice_threes32, [20, 185])
    win.blit(YACHT.dice_fours32, [20, 225])
    win.blit(YACHT.dice_fives32, [20, 265])
    win.blit(YACHT.dice_sixes32, [20, 305])
    if LOAD[9] == False:
        win.blit(YACHT.text_ace_b, [65, 112])
        win.blit(YACHT.text_deuces_b, [65, 152])
        win.blit(YACHT.text_threes_b, [65, 192])
        win.blit(YACHT.text_fours_b, [65, 232])
        win.blit(YACHT.text_fives_b, [65, 272])
        win.blit(YACHT.text_sixes_b, [65, 312])
        win.blit(YACHT.text_subtotal_b, [34, 360])
    elif LOAD[9] == True:
        win.blit(YACHT.text_ace_w, [65, 112])
        win.blit(YACHT.text_deuces_w, [65, 152])
        win.blit(YACHT.text_threes_w, [65, 192])
        win.blit(YACHT.text_fours_w, [65, 232])
        win.blit(YACHT.text_fives_w, [65, 272])
        win.blit(YACHT.text_sixes_w, [65, 312])
        win.blit(YACHT.text_subtotal_w, [34, 360])

    # choice score
    pygame.draw.rect(win,BOARDCOLOR, [15, 405, 340, 40], 2)
    pygame.draw.line(win, BOARDCOLOR, [155, 405], [155, 445], 4)
    pygame.draw.line(win, BOARDCOLOR, [255, 405], [255, 445], 1)
    win.blit(YACHT.choice32, [20, 410])
    if LOAD[9] == False:
        win.blit(YACHT.text_choice_b, [65, 415])
    elif LOAD[9] == True:
        win.blit(YACHT.text_choice_w, [65, 415])
    
    # lower section
    pygame.draw.rect(win, BOARDCOLOR, [15, 450, 340, 200], 2)
    pygame.draw.line(win, BOARDCOLOR, [15, 490], [355, 490], 2)
    pygame.draw.line(win, BOARDCOLOR, [15, 530], [355, 530], 2)
    pygame.draw.line(win, BOARDCOLOR, [15, 570], [355, 570], 2)
    pygame.draw.line(win, BOARDCOLOR, [15, 610], [355, 610], 2)
    pygame.draw.line(win, BOARDCOLOR, [155, 450], [155, 650], 4)
    pygame.draw.line(win, BOARDCOLOR, [255, 450], [255, 650], 1)
    win.blit(YACHT.fourofakind32, [20, 455])
    win.blit(YACHT.fullhouse32, [20, 495])
    win.blit(YACHT.sstraight32, [20, 535])
    win.blit(YACHT.lstraight32, [20, 575])
    win.blit(YACHT.yacht32, [20, 615])
    if LOAD[9] == False:
        win.blit(YACHT.text_fourofakind_b, [65, 460])
        win.blit(YACHT.text_fullhouse_b, [65, 500])
        win.blit(YACHT.text_sstraight_b, [65, 540])
        win.blit(YACHT.text_lstraight_b, [65, 580])
        win.blit(YACHT.text_yacht_b, [65, 620])
    elif LOAD[9] == True:
        win.blit(YACHT.text_fourofakind_w, [65, 460])
        win.blit(YACHT.text_fullhouse_w, [65, 500])
        win.blit(YACHT.text_sstraight_w, [65, 540])
        win.blit(YACHT.text_lstraight_w, [65, 580])
        win.blit(YACHT.text_yacht_w, [65, 620])        
    
    # total
    pygame.draw.rect(win, BOARDCOLOR, [15, 655, 340, 50], 2)
    pygame.draw.line(win, BOARDCOLOR, [155, 655], [155, 705], 4)
    pygame.draw.line(win, BOARDCOLOR, [255, 655], [255, 705], 1)
    if LOAD[9] == False:
        win.blit(YACHT.text_total_b, [53, 670])
    elif LOAD[9] == True:
         win.blit(YACHT.text_total_w, [53, 670])

def drawScore(win, side, board, LOAD, newScore=None, total= None):
    for i, eachPlayer in enumerate(board):
        for j, oldScore in enumerate(eachPlayer):
            # Upper
            if j < 6:
                height = 100 + 40 * j
            # Choice
            elif j == 6: 
                height = 405
            # Lower
            else:
                height = 450 + 40 * (j - 7)

            if oldScore[1] != -1:
                if oldScore[0] > 9:
                    width = 190 + 100 * i
                else:
                    width = 200 + 100 * i
                putNum(win, oldScore[0], (width, height), LOAD)
            else:
                if newScore != None and side == i:
                    if newScore[j] > 9:
                        width = 190 + 100 * i
                    else:
                        width = 200 + 100 * i
                    putGreyNum(win, newScore[j], (width, height))
    
    for i in range(len(total)):
        for j in range(len(total[i])):
            if j == 1 or j == 2 or j == 4:
                if total[i][j] > 9:
                    width = 190 + 100 * i 
                else:
                    width = 200 + 100 * i
                
                if j == 1:
                    height = 332
                elif j == 2:
                    height = 363
                elif j == 4:
                    height = 660
                putNum(win, total[i][j], (width ,height), LOAD)

def drawButton(win, turn, online, LOAD):
    if turn < 3:
        if LOAD[9] == False:
            win.blit(YACHT.ROLL_b, [900, 500])
        elif LOAD[9] == True:
            win.blit(YACHT.ROLL_w, [900, 500])
    if online == True:
        if LOAD[9] == False:
            win.blit(YACHT.SURREND_b, [650, 10])
        elif LOAD[9] == True:
            win.blit(YACHT.SURREND_w, [650, 10])
    else:
        if LOAD[9] == False:
            win.blit(YACHT.QUIT_b, [1000, 10])
        elif LOAD[9] == True:
            win.blit(YACHT.QUIT_w, [1000, 10])
        

def drawEtc(win, side, LOAD):
    if LOAD[9] == False:
        win.blit(YACHT.PLAYER_b, [400, 50])
        win.blit(YACHT.TURN_b, [550, 50])
    elif LOAD[9] == True:
        win.blit(YACHT.PLAYER_w, [400, 50])
        win.blit(YACHT.TURN_w, [550, 50])
    putLargeNum(win, side + 1, [500, 30], LOAD)

def drawHelp(win, helpon):
    win.blit(HELP.HELPS, [1150, 715])
    if helpon == True:
        pygame.draw.rect(win, (200, 20, 20), (5, 5, 357, 710), 4)  #score board
        pygame.draw.rect(win, (200, 20, 20), (370, 10, 380, 90), 4)  #player / turn
        pygame.draw.rect(win, (200, 20, 20), (368, 135, 368, 110), 4)  
        #pygame.draw.rect(win, (200, 20, 20), (980, 30, 186, 70), 4)  #QUIT THIS GAME
        pygame.draw.rect(win, (200, 20, 20), (500, 260, 570, 165), 4)
        pygame.draw.rect(win, (200, 20, 20), (850, 510, 340, 128), 4)
        win.blit(HELP.SCORE_BOARD, [4, 0])

        win.blit(HELP.ACES, [195, 100])
        win.blit(HELP.TWOS, [195, 140])
        win.blit(HELP.THREE, [195, 180])
        win.blit(HELP.FOURS, [195, 220])
        win.blit(HELP.FIVES, [195, 260])
        win.blit(HELP.SIXES, [195, 300])

        win.blit(HELP.CHOICE, [195, 405])
        win.blit(HELP.FOUR_OF_A_KIND, [195, 450])
        win.blit(HELP.F_HOUSE, [195, 490])
        win.blit(HELP.S_STRAIGHT, [195, 530])
        win.blit(HELP.L_STRAIGHT, [195, 570])
        win.blit(HELP.YACHT, [195, 610])

        win.blit(HELP.PLAYER_TURN, [380, 0])
        win.blit(HELP.SAVING_DICES, [385, 190])
        win.blit(HELP.DICES, [900, 250])
        win.blit(HELP.TO_DO_DICES, [860, 580])

def prompt(win):
    emptyRoundRect(win, (255, 255, 255), (300, 350, 600, 160), 4, 4)

    win.blit(YACHT.MESSAGE[0], (350, 365))
    win.blit(YACHT.MESSAGE[1], (350, 390))

    win.blit(YACHT.YES, (445, 440))
    win.blit(YACHT.NO, (605, 440))
    pygame.draw.rect(win, (255, 255, 255), (440, 440, 100, 50), 2)
    pygame.draw.rect(win, (255, 255, 255), (600, 440, 100, 50), 2)

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 440 < event.pos[1] < 490:
                    if 440 < event.pos[0] < 540:
                        return True
                    elif 600 < event.pos[0] < 700:
                        return False

