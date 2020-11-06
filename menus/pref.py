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
from tools.utils import emptyRoundRect, solidRoundRect

# 참 거짓을 문자열에서 반환한다


def makeBool(x):
    return x.strip() == "True" or x.strip() == "true"

# 사용자 설정 택스트 파일로 저장


def save(*params):
    print(params)
    text = ""
    text += "sounds=" + str(params[0]) + '\n'
    text += "themes_brown=" + str(params[1]) + '\n'
    text += "themes_green=" + str(params[2]) + '\n'
    text += "themes_black=" + str(params[3]) + '\n'
    text += "themes_sky=" + str(params[4]) + '\n'

    with open(os.path.join("res", "preferences.txt"), "w") as f:
        f.write(text)

# 사용자 설정 로드


def load():
    with open(os.path.join("res", "preferences.txt"), "r") as f:
        return [makeBool(i.split("=")[1]) for i in f.read().splitlines()]

def load_themes():
    with open(os.path.join("res", "preferences.txt"), "r") as f:
        result = f.readlines()
        temp = result[1].split("=")
        result_list = temp[1].split("\n")
        print(result_list[0])
        return result_list
# 0, 1, 2 들을 리턴

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
        print(prefs)
        win.blit(PREF.COLON, (400, 150))
        if prefs[0]==True:
            emptyRoundRect(win, (255, 255, 255),
                           (440, 152, 250, 100), 8, 2)
        elif prefs[0]==False:
            emptyRoundRect(win, (255, 255, 255),
                           (750, 152, 250, 100), 8, 2)
        win.blit(PREF.TRUE, (470, 150))
        win.blit(PREF.FALSE, (770, 150))

    # 백그라운드
    win.blit(PREF.THEMES, (90, 250))
    win.blit(PREF.COLON, (400, 250))

    emptyRoundRect(win, (255, 255, 255),(490, 265, 84, 84), 8, 2) # 우드 선택
    emptyRoundRect(win, (255, 255, 255),(590, 265, 84, 84), 8, 2) # 초록 선택
    emptyRoundRect(win, (255, 255, 255),(690, 265, 84, 84), 8, 2) # 검정 선택
    emptyRoundRect(win, (255, 255, 255),(790, 265, 84, 84), 8, 2) # 하늘 선택

    solidRoundRect(win, (185, 120, 90), (500, 275, 64, 64), 10)  # 우드
    solidRoundRect(win, (0, 128, 0), (600, 275, 64, 64), 10)  #  초록
    solidRoundRect(win, (65, 65, 65), (700, 275, 64, 64), 10)  # 검정 
    solidRoundRect(win, (100, 200, 200), (800, 275, 64, 64), 10) # 하늘

    # 다이스
    win.blit(PREF.DICES, (90, 350))
    win.blit(PREF.COLON, (400, 350))

    emptyRoundRect(win, (255, 255, 255),(490, 370, 84, 84), 8, 2) # 흰주사위 선택
    emptyRoundRect(win, (255, 255, 255),(590, 370, 84, 84), 8, 2) # 빨강 주사위 선택
    emptyRoundRect(win, (255, 255, 255),(690, 370, 84, 84), 8, 2) # 파랑 주사위 선택
    
    win.blit(PREF.WHITEDICE, (500, 380))
    win.blit(PREF.REDDICE, (600, 380))
    win.blit(PREF.BLUEDICE, (700, 380))

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
                    if 152 < event.pos[1] < 252:
                        if 440 < event.pos[0] < 690:
                            prefs[0] = True
                        if 750 < event.pos[0] < 1000:
                            prefs[0] = False
                    if 265 < event.pos[1] < 349:
                        # 갈색 뒷배경 클릭
                        if 490 < event.pos[0] < 574:
                            prefs[1] = True
                            prefs[2] = False
                            prefs[3] = False
                            prefs[4] = False
                        # 초록 뒷배경 클릭
                        if 590 < event.pos[0] < 674:
                            prefs[1] = False
                            prefs[2] = True
                            prefs[3] = False
                            prefs[4] = False
                        # 검정 뒷배경 클릭
                        if 690 < event.pos[0] < 774:
                            prefs[1] = False
                            prefs[2] = False
                            prefs[3] = True
                            prefs[4] = False
                        # 하늘색 뒷배경 클릭
                        if 790 < event.pos[0] < 874:
                            prefs[1] = False
                            prefs[2] = False
                            prefs[3] = False
                            prefs[4] = True

        pygame.display.update()
