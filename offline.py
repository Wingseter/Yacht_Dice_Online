import pygame
from tools.utils import emptyRoundRect
from tools.textBox import textBox
import random


def showProgress(win):
    win.fill((100,111,155))
    emptyRoundRect(win, (255, 255, 255), (25, 30, 1150, 700), 7, 7)

    emptyRoundRect(win, (255, 255, 255), (500, 70, 40, 70), 7, 7)


    

def main(win):   
    finish = False
    clock = pygame.time.Clock()
    red = pygame.color.Color('#FF0000')
    white = pygame.color.Color('#FFFFFF')
    black = pygame.color.Color('#000000')
    count = 0
    size = [500, 500]
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

    counter, text = 10, '10'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)

    showProgress(win)

    #game loop(로직 생성)
    while not finish:

        #주사위 굴러간다
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and roll == False:
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
        clock.tick(100)

        for event in pygame.event.get(): #발생한 이벤트 리스트 가져오기
            if event.type == pygame.QUIT: #파이 게임이 끝났으면
                finish = True 

        #타이머 counting
        for e in pygame.event.get():
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
