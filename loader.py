import os.path
import pygame

# 폰트 정의
pygame.font.init()
FONT = os.path.join("res", "font", "Kenney Mini Square.ttf")
huge = pygame.font.Font(FONT, 577)
head = pygame.font.Font(FONT, 150)
large = pygame.font.Font(FONT, 120)
medium = pygame.font.Font(FONT, 80)
small = pygame.font.Font(FONT, 50)
vsmall = pygame.font.Font(FONT, 30)
fvsmall = pygame.font.Font(FONT, 20)

# 색상 정의
WHITE = (255, 255, 255)
GREY = (180, 180, 180)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (200, 20, 20)

class MAIN:
    ICON = pygame.image.load(os.path.join("res", "img", "icon.gif"))
    TITLE = head.render("Yacht Dice", True, RED)
    OFFLINE = medium.render("Offline", True, WHITE)
    OFFLINE_H = medium.render("Offline", True, GREY)
    ONLINE = medium.render("Online", True, WHITE)
    ONLINE_H = medium.render("Online", True, GREY)
    OPTION = medium.render("Option", True, WHITE)
    OPTION_H = medium.render("Option", True, GREY)
    QUIT = medium.render("Quit", True, WHITE)
    QUIT_H = medium.render("Quit", True, GREY)

class ONLINEMENU:
    HEAD = large.render("Online", True, WHITE)
    with open(os.path.join("res", "texts", "online.txt")) as f:
        TEXT = [vsmall.render(i, True, WHITE)
        for i in f.read().splitlines()]
    
    ENTER = small.render("Input Server IP", True, WHITE)
    CLICK = vsmall.render("Click Here", True, WHITE)
    BACK = vsmall.render("Go Back", True, WHITE)
    CONNECT = small.render("Connect", True, WHITE)
        
class OFFLINEGAME:
    GIVEUP = fvsmall.render("Give up", True, RED)
    GIVEUP_H = fvsmall.render("Give up", True, GREY)
    WINNER = fvsmall.render("WIN", True, RED)
    WIN_APPEARING = huge.render("WIN", True, GREEN)