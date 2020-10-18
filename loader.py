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

font_obj16 = pygame.font.Font("res/font/FFFFORWA.TTF", 16)
font_obj18 = pygame.font.Font("res/font/FFFFORWA.TTF", 18)
font_obj24 = pygame.font.Font("res/font/FFFFORWA.TTF", 24)
font_obj32 = pygame.font.Font("res/font/FFFFORWA.TTF", 32)
font_obj52 = pygame.font.Font("res/font/FFFFORWA.TTF", 52)
 
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
        vsmall.render("you will play second.", True, WHITE),
    )
    MSG2 = (
        vsmall.render("Player", True, WHITE),
        vsmall.render("wants to play with you.", True, WHITE),
        vsmall.render("you will play first.", True, WHITE),
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

class YACHT:
    dice32 = pygame.image.load("res/img/dice32.png")
    dice64 = pygame.image.load("res/img/dice64.png")
    dice_ace32 = pygame.image.load("res/img/ace32.png")
    dice_deuces32 = pygame.image.load("res/img/deuces32.png")
    dice_threes32 = pygame.image.load("res/img/threes32.png")
    dice_fours32 = pygame.image.load("res/img/fours32.png")
    dice_fives32 = pygame.image.load("res/img/fives32.png")
    dice_sixes32 = pygame.image.load("res/img/sixes32.png")
    dice_ace64 = pygame.image.load("res/img/ace64.png")
    dice_deuces64 = pygame.image.load("res/img/deuces64.png")
    dice_threes64 = pygame.image.load("res/img/threes64.png")
    dice_fours64 = pygame.image.load("res/img/fours64.png")
    dice_fives64 = pygame.image.load("res/img/fives64.png")
    dice_sixes64 = pygame.image.load("res/img/sixes64.png")
    choice32 = pygame.image.load("res/img/choice32.png")
    fourofakind32 = pygame.image.load("res/img/quads32.png")
    fullhouse32 = pygame.image.load("res/img/fullhouse32.png")
    sstraight32 = pygame.image.load("res/img/sstraight32.png")
    lstraight32 = pygame.image.load("res/img/lstraight32.png")
    yacht32 = pygame.image.load("res/img/yacht32.png")

    text_title = font_obj52.render("Yacht Dice", False, WHITE)
    text_total = font_obj18.render("Total", False, WHITE)
    text_ace = font_obj16.render("Ace", False, WHITE)
    text_deuces = font_obj16.render("Deuces", False, WHITE)
    text_threes = font_obj16.render("Threes", False, WHITE)
    text_fours = font_obj16.render("Fours", False, WHITE)
    text_fives = font_obj16.render("Fives", False, WHITE)
    text_sixes = font_obj16.render("Sixes", False, WHITE)
    text_subtotal = font_obj18.render("SubTotal", False, WHITE)
    text_choice = font_obj16.render("Choice", False, WHITE)
    text_fourofakind = font_obj16.render("Quads", False, WHITE)
    text_fullhouse = font_obj16.render("F.House", False, WHITE)
    text_sstraight = font_obj16.render("S.Strght", False, WHITE)
    text_lstraight = font_obj16.render("L.Strght", False, WHITE)
    text_yacht = font_obj16.render("Yacht", False, WHITE)
    text_com = font_obj24.render("COM", False, WHITE)
    text_player = font_obj24.render("P1", False, WHITE)