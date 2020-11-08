'''
This file is a part of My-PyChess application.
In this file, we manage the preferences menu which is called when user clicks
preferences button on main menu.

We also define functions to save and load user preferences.

Level of development = STABLE
'''

import os.path
import pygame
from loader import PREF
from tools.utils import emptyRoundRect

# 참 거짓을 문자열에서 반환한다
def makeBool(x):
    return x.strip() == "True" or x.strip() == "true"

# 사용자 설정 택스트 파일로 저장
def save(*params):
    text = ""
    text += "sounds = " + str(params[0]) + '\n'
    
    with open(os.path.join("res", "preferences.txt"), "w") as f:
        f.write(text)

# 사용자 설정 로드
def load():
    with open(os.path.join("res", "preferences.txt"), "r") as f:
        return [makeBool(i.split("=")[1]) for i in f.read().splitlines()]
    
# 사용자 설정 화면
def prompt(win):
    emptyRoundRect(win, (255, 255, 255), (300, 350, 600, 160), 4, 4)

    win.blit(PREF.PROMPT[0], (350, 365))
    win.blit(PREF.PROMPT[1], (350, 390))

    win.blit(PREF.YES, (445, 440))
    win.blit(PREF.NO, (605, 440))
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

# 옵션 화면 설정
def showScreen(win, prefs):
    win.fill((100, 100, 200))
    
    emptyRoundRect(win, (255, 255, 255), (100, 10, 1000, 120), 20, 4)
    emptyRoundRect(win, (255, 255, 255), (10, 150, 1150, 500), 12, 4)
    win.blit(PREF.HEAD, (200, -20))

    
    win.blit(PREF.SOUNDS, (90, 150))

    for i in range(len(prefs)):
        win.blit(PREF.COLON, (400, 150 + (i * 60)))
        if prefs[i]:
            emptyRoundRect(win, (255, 255, 255), (440, 152 + (100 * i), 250, 100), 8, 2)
        else:
            emptyRoundRect(win, (255, 255, 255), (750, 152 + (100 * i), 250, 100), 8, 2)
        win.blit(PREF.TRUE, (470, 150 + (i * 100)))
        win.blit(PREF.FALSE, (770, 150 + (i * 100)))
    
    emptyRoundRect(win, (255, 255, 255), (470, 652, 250, 100), 10, 3)
    win.blit(PREF.BSAVE, (500, 650))

def main(win):
    prefs = load()
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        showScreen(win, prefs)
        for event in pygame.event.get():
            if event.type == pygame.QUIT and prompt(win):
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 470 < event.pos[0] < 720 and 652 < event.pos[1] < 752:
                    save(*prefs)
                    return
                for cnt in range(len(prefs)):
                    if 152 + cnt*100 < event.pos[1] < 252 + cnt*100:
                        if 440 < event.pos[0] < 690:
                            prefs[cnt] = True
                        if 750 < event.pos[0] < 1000:
                            prefs[cnt] = False                  
        pygame.display.update()
