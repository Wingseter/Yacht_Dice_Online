import pygame
from tools.utils import emptyRoundRect
from tools.textBox import textBox
import random
from loader import OFFLINEGAME

def showProgress(win):
    win.fill((100,111,155))
    emptyRoundRect(win, (255, 255, 255), (25, 30, 1150, 700), 7, 5)    #판
    emptyRoundRect(win, (255, 255, 255), (44, 390, 580, 320), 4, 5)    #주사위 공간
    emptyRoundRect(win, (255, 255, 255), (40, 40, 100, 40), 7, 5)       #기권
    emptyRoundRect(win, (255, 255, 255), (650, 40, 510, 670), 7, 5)    #족보 저장공간


def main(win):  
    finish = False
    clock = pygame.time.Clock()
    
    red = pygame.color.Color('#FF0000')
    white = pygame.color.Color('#FFFFFF')
    black = pygame.color.Color('#000000')
    count = 0
    size = [500, 500]

    #기권
    giveup = (55, 45, 70, 40)

    #주사위
    roll = False
    x = 250
    y = 250
    x2 = 250
    y2 = 250
    x3 = 250
    y3 = 250
    x4 = 250
    y4 = 250
    x5 = 250
    y5 = 250
    x6 = 250
    y6 = 250
    done = False

    #타이머
    counter, text = 10, '10'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)

    #game loop(로직 생성)
    while not finish:
        showProgress(win)
        #기권
        win.blit(OFFLINEGAME.GIVEUP, giveup[:2])

        for event in pygame.event.get(): #발생한 이벤트 리스트 가져오기
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN: #Give up 누르면 게임 종료
                x, y = event.pos
                if giveup[0] < x < sum(giveup[::2]) and giveup[1] < y < sum(giveup[1::2]):
                    finish = True 
            elif event.type == pygame.QUIT: #파이 게임이 끝났으면
                finish = True 
        #space누르면 주사위 굴러감
        keys = pygame.key.get_pressed()         
        if keys[pygame.K_SPACE] and roll == False:     #스페이스 누르면 주사위 구르기 or 멈추기
            roll = True
        elif roll == True and keys[pygame.K_SPACE]:
            roll = False
        if roll == True:
            count +=1
            if count == 15:
                    count = 0
                    num = random.randrange(1, 7)
                    if num == 1:
                        x = 250
                        y = 250
                        x2 = 250
                        y2 = 250
                        x3 = 250
                        y3 = 250
                        x4 = 250
                        y4 = 250
                        x5 = 250
                        y5 = 250
                        x6 = 250
                        y6 = 250
                    elif num == 2:
                        x = 210
                        y = 210
                        x2 = 210
                        y2 = 210
                        x3 = 210
                        y3 = 210
                        x4 = 210
                        y4 = 210
                        x5 = 210
                        y5 = 210
                        x6 = 290
                        y6 = 290
                    elif num == 3:
                        x = 210
                        y = 210
                        x2 = 210
                        y2 = 210
                        x3 = 210
                        y3 = 210
                        x4 = 210
                        y4 = 210
                        x5 = 290
                        y5 = 290
                        x6 = 250
                        y6 = 250
                    elif num == 4:
                        x = 210
                        y = 210
                        x2 = 290
                        y2 = 290
                        x3 = 290
                        y3 = 210
                        x4 = 210
                        y4 = 290
                        x5 = 210
                        y5 = 210
                        x6 = 210
                        y6 = 210
                    elif num == 5:
                        x = 210
                        y = 210
                        x2 = 290
                        y2 = 290
                        x3 = 290
                        y3 = 210
                        x4 = 210
                        y4 = 290
                        x5 = 250
                        y5 = 250
                        x6 = 250
                        y6 = 250
                    else:
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
        clock.tick(100000)

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