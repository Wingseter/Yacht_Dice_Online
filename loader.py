import os.path
import pygame

# 폰트 정의
pygame.font.init()
FONT = os.path.join("res", "font", "Kenney Mini Square.ttf")
head = pygame.font.Font(FONT, 150)
large = pygame.font.Font(FONT, 120)
medium = pygame.font.Font(FONT, 80)
small = pygame.font.Font(FONT, 50)
vsmall = pygame.font.Font(FONT, 30)

# 색상 정의
WHITE = (255, 255, 255)
GREY = (180, 180, 180)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (200, 20, 20)

# 숫자 배열
NUM = [vsmall.render(str(i), True, WHITE) for i in range(10)]
LNUM = [small.render(str(i), True, WHITE) for i in range(10)]

# 숫자 입력
def putNum(win, num, pos):
    for cnt, i in enumerate(list(str(num))):
        win.blit(NUM[int(i)], (pos[0] + (cnt * 20), pos[1]))

# 큰 숫자 입력
def putLargeNum(win, num, pos):
    for cnt, i in enumerate(list(str(num))):
        win.blit(LNUM[int(i)], (pos[0] + (cnt * 30), pos[1]))

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

class ONLINE:
    TRYCONN = vsmall.render("Trying to connect to server....", True, WHITE)
    ERR = [
        vsmall.render("[ERR 1] Couldn't find the server...", True, WHITE),
        vsmall.render("[ERR 2] Server refused connection..,", True, WHITE),
        vsmall.render("[ERR 3] Server is full..,", True, WHITE),
        vsmall.render("[ERR 4] The server is Locked...", True, WHITE),
    ]
        
    EMPTY = small.render("No one's online", True, WHITE)

    LOBBY = large.render("Online Lobby", True, WHITE)
    LIST = small.render("List of Players", True, WHITE)
    PLAYER = vsmall.render("Player", True, WHITE)
    PLAYER2 = small.render("Player", True, WHITE)
    DOT = vsmall.render(".", True, WHITE)

    ACTIVE = vsmall.render("ACTIVE", True, GREEN)
    BUSY = vsmall.render("BUSY", True, RED)
    REQ = vsmall.render("Send Request", True, WHITE)
    YOUARE = medium.render("You Are", True, WHITE)

    REFRESH = pygame.image.load(os.path.join("res", "img", "refresh.png"))

    MSG1 = (
        vsmall.render("Please wait for the other player to", True, WHITE),
        vsmall.render("accept your request. Game will begin", True, WHITE),
    )
    MSG2 = (
        vsmall.render("Player", True, WHITE),
        vsmall.render("wants to play with you.", True, WHITE),
    )

    OPPQUIT = small.render("Your Opponent has left", True, WHITE)
    RESIGN = small.render("Your Opponent has resigned", True, WHITE)
    DRAWAGREED = small.render("Draw has been agreed", True, WHITE)

    DRAW = (
        vsmall.render("Sent a request to your opponent for", True, WHITE),
        vsmall.render("draw, wait for reply.", True, WHITE),
    )

    DRAW2 = (
        vsmall.render("Your opponent is requesting for a", True, WHITE),
        vsmall.render("draw, please reply.", True, WHITE),
    )

    NO = small.render("NO", True, WHITE)
    OK = small.render("OK", True, WHITE)
