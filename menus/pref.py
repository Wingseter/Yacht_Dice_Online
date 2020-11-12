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
    #print(params)
    text = ""
    text += "sounds=" + str(params[0]) + '\n'
    text += "themes_brown=" + str(params[1]) + '\n'
    text += "themes_green=" + str(params[2]) + '\n'
    text += "themes_black=" + str(params[3]) + '\n'
    text += "themes_sky=" + str(params[4]) + '\n'
    text += "dices_white=" + str(params[5]) + '\n'
    text += "dices_red=" + str(params[6]) + '\n'
    text += "dices_blue=" + str(params[7]) + '\n'
    text += "charactor=" + str(params[8]) + '\n'
    text += "font=" + str(params[9]) + '\n'

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

    win.blit(PREF.SOUNDS, (90, 160))

    for i in range(len(prefs)):
        win.blit(PREF.COLON, (400, 160))
        if prefs[0]==True:
            emptyRoundRect(win, (255, 255, 255),
                           (465, 162, 170, 60), 8, 2)
        elif prefs[0]==False:
            emptyRoundRect(win, (255, 255, 255),
                           (755, 162, 170, 60), 8, 2)
    win.blit(PREF.TRUE, (490, 160))
    win.blit(PREF.FALSE, (770, 160))

    # 백그라운드
    win.blit(PREF.THEMES, (90, 230))
    win.blit(PREF.COLON, (400, 230))

    for i in range(len(prefs)):
        if prefs[1] == True:
            emptyRoundRect(win, (255, 255, 255),(495, 235, 60, 60), 8, 2) # 우드 선택
        elif prefs[2] == True:
            emptyRoundRect(win, (255, 255, 255),(595, 235, 60, 60), 8, 2) # 초록 선택
        elif prefs[3] == True:
            emptyRoundRect(win, (255, 255, 255),(695, 235, 60, 60), 8, 2) # 검정 선택
        elif prefs[4] == True:
            emptyRoundRect(win, (255, 255, 255),(795, 235, 60, 60), 8, 2) # 하늘 선택
    solidRoundRect(win, (185, 120, 90), (500, 240, 50, 50), 10)  # 우드
    solidRoundRect(win, (0, 128, 0), (600, 240, 50, 50), 10)  #  초록
    solidRoundRect(win, (65, 65, 65), (700, 240, 50, 50), 10)  # 검정 
    solidRoundRect(win, (100, 200, 200), (800, 240, 50, 50), 10) # 하늘

    # 다이스
    win.blit(PREF.DICES, (90, 300))
    win.blit(PREF.COLON, (400, 300))
    

    for i in range(len(prefs)):
        if prefs[5] == True:
            emptyRoundRect(win, (255, 255, 255),(495, 310, 60, 60), 8, 2) # 흰주사위 선택
        elif prefs[6] == True:
            emptyRoundRect(win, (255, 255, 255),(595, 310, 60, 60), 8, 2) # 빨강 주사위 선택
        elif prefs[7] == True:
            emptyRoundRect(win, (255, 255, 255),(695, 310, 60, 60), 8, 2) # 파랑 주사위 선택
    win.blit(PREF.WHITEDICE, (500, 315))
    win.blit(PREF.REDDICE, (600, 315))
    win.blit(PREF.BLUEDICE, (700, 315))

    # 폰트 색 선택
    win.blit(PREF.FONTS, (90, 370))
    win.blit(PREF.COLON, (400, 370))

    for i in range(len(prefs)):
        if prefs[9] == True:
            emptyRoundRect(win, (255, 255, 255),(495, 375, 60, 60), 8, 2) # 흰 폰트 선택
        elif prefs[9] == False:
            emptyRoundRect(win, (255, 255, 255),(595, 375, 60, 60), 8, 2) # 검정 폰트 선택
    solidRoundRect(win, (255, 255, 255), (500, 380, 50, 50), 10)  # 흰 폰트
    emptyRoundRect(win, (255, 255, 255), (600, 380, 50, 50), 10, 1) # 검정 폰트

    # 캐릭터 선택창
    win.blit(PREF.CHARACTOR, (90, 500))
    win.blit(PREF.COLON, (400, 500))
    
    for i in range(len(prefs)):
        win.blit(PREF.COLON, (400, 160))
        if prefs[8]==True:
            emptyRoundRect(win, (255, 255, 255),
                        (445, 480, 275, 130), 8, 2)
        elif prefs[8]==False:
            emptyRoundRect(win, (255, 255, 255),
                        (795, 480, 310, 130), 8, 2)
    win.blit(PREF.TXTLISA, (600, 500))
    win.blit(PREF.TXTBABEL, (950, 500))
    win.blit(PREF.ICONLISA, (450, 485))
    win.blit(PREF.ICONBABEL, (800, 485))

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
                    if 170 < event.pos[1] < 220:
                        if 450 < event.pos[0] < 590:
                            prefs[0] = True
                        if 730 < event.pos[0] < 970:
                            prefs[0] = False
                    # 뒷배경 바꾸기
                    if 215 < event.pos[1] < 300:
                        # 갈색 뒷배경 클릭
                        if 500 < event.pos[0] < 550:
                            prefs[1] = True
                            prefs[2] = False
                            prefs[3] = False
                            prefs[4] = False
                        # 초록 뒷배경 클릭
                        if 600 < event.pos[0] < 650:
                            prefs[1] = False
                            prefs[2] = True
                            prefs[3] = False
                            prefs[4] = False
                        # 검정 뒷배경 클릭
                        if 700 < event.pos[0] < 750:
                            prefs[1] = False
                            prefs[2] = False
                            prefs[3] = True
                            prefs[4] = False
                        # 하늘색 뒷배경 클릭
                        if 800 < event.pos[0] < 850:
                            prefs[1] = False
                            prefs[2] = False
                            prefs[3] = False
                            prefs[4] = True
                    # 주사위 바꾸기
                    if 315 < event.pos[1] < 365:
                        # 흰 주사위
                        if 490 < event.pos[0] < 540:
                            prefs[5] = True
                            prefs[6] = False
                            prefs[7] = False
                        # 빨강 주사위
                        if 590 < event.pos[0] < 640:
                            prefs[5] = False
                            prefs[6] = True
                            prefs[7] = False
                        # 파랑 주사위
                        if 690 < event.pos[0] < 740:
                            prefs[5] = False
                            prefs[6] = False
                            prefs[7] = True
                # 캐릭터 바꾸기
                if 480 < event.pos[1] < 630:
                    # 리사
                    if 445 < event.pos[0] < 720:
                        prefs[8] = True
                    # 바벨
                    if 795 < event.pos[0] < 1070:
                        prefs[8] = False
                # 폰트 색 정하기
                if 380 < event.pos[1] < 430:
                        # 흰 폰트
                        if 490 < event.pos[0] < 540:
                            prefs[9] = True
                        # 검정
                        if 590 < event.pos[0] < 640:
                            prefs[9] = False

        pygame.display.update()
