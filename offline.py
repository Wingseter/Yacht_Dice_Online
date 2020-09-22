import pygame
import Countdown

pygame.init()

ourScreen = pygame.display.set_mode((1200, 750))
pygame.display.set_caption('Yacht_Dice')

clock = pygame.time.Clock()

finish = False
colorBlue = True

clock = pygame.time.Clock()
counter, text = 30, '30'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

#game loop(로직 생성)
while not finish:
    for event in pygame.event.get(): #발생한 이벤트 리스트 가져오기
        if event.type == pygame.QUIT: #파이 게임이 끝났으면
            finish = True 

    ourScreen.fill((250,209,155))
  
    color1 = (255,255,255)
    color2 = (250,222,255)
    pygame.draw.rect(ourScreen, color1, pygame.Rect(30,30,120,120))
    pygame.draw.rect(ourScreen, color2, pygame.Rect(1000,20,77,70))
    # update the screen

#    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
          counter -= 1
          text = str(counter).rjust(3) if counter > 0 else 'boom!'
        if e.type == pygame.QUIT: break
        else:

          ourScreen.blit(font.render(text, True, (0, 0, 0)), (1000,20,30,40))
          pygame.display.flip()
          clock.tick(60)
          continue
          break

"""
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: #스페이스바 누르면 색
        colorBlue = not colorBlue
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y-=3
    if pressed[pygame.K_DOWN]: y+=3
    if pressed[pygame.K_LEFT]: x-=3
    if pressed[pygame.K_RIGHT]: x+=3

    if colorBlue: color = (0,128,255) #파란색으로 변경
    else: color = (255,255,255) #흰색으로 변경

    pygame.draw.rect(ourScreen, color, pygame.Rect(x,y,60,60))  #ourScreen 에 사각형 그리고, 색 지정해주기, 좌표와 크기 지정
    pygame.display.flip() #display 업데이트 (flip()또는 update())

    clock.tick(60)
 """



"""
def setup():
    frameRate(60)
    size(500, 500)
    noLoop()

def draw(self):
  background('#777777')

  noStroke()
  fill('#ffffff')
  rectMode(CENTER)
  rect(250, 250, 100, 100)

  fill('#333333')
  ecllipse(250,250,20,20)
"""