import pygame
from tools.utils import emptyRoundRect
from tools.textBox import textBox
import random
from loader import OFFLINEGAME
import time

def showProgress(win):
    win.fill((100,111,155))
    emptyRoundRect(win, (255, 255, 255), (25, 30, 1150, 700), 7, 5)    #판
    emptyRoundRect(win, (255, 255, 255), (44, 390, 580, 320), 4, 5)    #주사위 공간
    emptyRoundRect(win, (255, 255, 255), (40, 40, 100, 40), 7, 5)      #기권
    emptyRoundRect(win, (255, 255, 255), (372, 40, 100, 40), 7, 5)      #승리
    emptyRoundRect(win, (255, 255, 255), (650, 40, 510, 670), 7, 5)    #족보 저장공간
    emptyRoundRect(win, (255, 255, 255), (650, 40, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 94, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 149, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 204, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 260, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 315, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 370, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 425, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 480, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 535, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 590, 510, 60), 7, 5)
    emptyRoundRect(win, (255, 255, 255), (650, 645, 510, 60), 7, 5)

def Winner(win, coordinate):
    clock = pygame.time.Clock()
    win_appearing = coordinate
    win.blit(OFFLINEGAME.WIN_APPEARING, win_appearing[:2])
    pygame.display.update()
    time.sleep(1)
    clock.tick(300)

def main(win):  
    finish = False
    clock = pygame.time.Clock()
    
    red = pygame.color.Color('#FF0000')
    white = pygame.color.Color('#FFFFFF')
    black = pygame.color.Color('#000000')
    count = 0
    size = [500, 500]

    #승리, 기권
    winner = (408, 45, 70, 40)
    giveup = (55, 45, 70, 40)

    #타이머
    counter, text = 10, '10'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)

    #game loop(로직 생성)
    while not finish:
        showProgress(win)
        #기권
        win.blit(OFFLINEGAME.GIVEUP, giveup[:2])
        win.blit(OFFLINEGAME.WINNER, winner[:2])
        for event in pygame.event.get(): #발생한 이벤트 리스트 가져오기
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN: #Give up 누르면 게임 종료
                x, y = event.pos
                if giveup[0] < x < sum(giveup[::2]) and giveup[1] < y < sum(giveup[1::2]):
                    finish = True 
                elif winner[0] < x < sum(winner[::2]) and winner[1] < y < sum(winner[1::2]):
                    coordinate = (200,100,500,500)
                    Winner(win, coordinate)
            elif event.type == pygame.QUIT: #파이 게임이 끝났으면
                finish = True 

        x = 210
        y = 210
        x2 = 290
        y2 = 290
        x3 = 290
        y3 = 210
        x4 = 210
        y4 = 290
        x5 = 210
        y5 = 250
        x6 = 290
        y6 = 250

        pygame.draw.rect(win, red, (200, 200, 100, 100))
        pygame.draw.circle(win, white, [x, y], 8)
        pygame.draw.circle(win, white, [x2, y2], 8)
        pygame.draw.circle(win, white, [x3, y3], 8)
        pygame.draw.circle(win, white, [x4, y4], 8)
        pygame.draw.circle(win, white, [x5, y5], 8)
        pygame.draw.circle(win, white, [x6, y6], 8)

        #타이머 counting
        for e in pygame.event.get(False):
            if e.type == pygame.USEREVENT: 
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else 'boom!'
            if e.type == pygame.QUIT: break
        else:
            win.blit(font.render(text, True, (0, 0, 0)), (1000,2,30,40))
            pygame.display.flip()
            clock.tick(60)
            continue
        break
