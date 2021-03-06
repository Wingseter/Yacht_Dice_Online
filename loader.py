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
BLUE = (0, 160, 230)

#백그라운드 색상 정의
BG_WOOD = (185, 120, 90)  # 우드
BG_GREEN = (0, 128, 0)  #  초록
BG_BLACK = (65, 65, 65)  # 검정 
BG_SKY = (100, 200, 200) # 하늘

# 숫자 배열
NUM_w = [vsmall.render(str(i), True, WHITE) for i in range(10)]
NUM_b = [vsmall.render(str(i), True, BLACK) for i in range(10)]
GREYNUM = [vsmall.render(str(i), True, GREY) for i in range(10)]
LNUM_w = [small.render(str(i), True, WHITE) for i in range(10)]
LNUM_b = [small.render(str(i), True, BLACK) for i in range(10)]

# 숫자 입력

def putNum(win, num, pos):
    for cnt, i in enumerate(list(str(num))):
        win.blit(NUM_w[int(i)], (pos[0] + (cnt * 20), pos[1]))

def putGreyNum(win, num, pos):
    for cnt, i in enumerate(list(str(num))):
        win.blit(GREYNUM[int(i)], (pos[0] + (cnt * 20), pos[1]))


def putLargeNum(win, num, pos):
    for cnt, i in enumerate(list(str(num))):
        win.blit(LNUM_w[int(i)], (pos[0] + (cnt * 30), pos[1]))

def putColorNum(win, num, pos, LOAD):
    for cnt, i in enumerate(list(str(num))):
        if LOAD[9] == False:
            win.blit(NUM_b[int(i)], (pos[0] + (cnt * 20), pos[1]))
        elif LOAD[9] == True:
            win.blit(NUM_w[int(i)], (pos[0] + (cnt * 20), pos[1]))
            
def putColorLargeNum(win, num, pos, LOAD):
    for cnt, i in enumerate(list(str(num))):
        if LOAD[9] == False:
            win.blit(LNUM_b[int(i)], (pos[0] + (cnt * 30), pos[1]))
        elif LOAD[9] == True:
            win.blit(LNUM_w[int(i)], (pos[0] + (cnt * 30), pos[1]))


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
    OPPQUIT = small.render("Your Opponent has left", True, WHITE)

    CHRLISA = pygame.image.load("res/img/charactor/1chr.png")
    CHRBABEL = pygame.image.load("res/img/charactor/2chr.png")


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
    COUNT = vsmall.render("WIN", True, WHITE)

    ACTIVE = vsmall.render("ACTIVE", True, GREEN)
    BUSY = vsmall.render("BUSY", True, RED)
    REQ = vsmall.render("Send Request", True, WHITE)
    YOUARE = medium.render("You Are", True, WHITE)

    REFRESH = pygame.image.load(os.path.join("res", "img", "refresh.png"))

    MSG1 = (
        vsmall.render("Please wait for the other player to", True, WHITE),
        vsmall.render("accept your request. Game will begin", True, WHITE),
        vsmall.render("you will play as PLAYER 2.", True, WHITE),
    )
    MSG2 = (
        vsmall.render("Player", True, WHITE),
        vsmall.render("wants to play with you.", True, WHITE),
        vsmall.render("you will play as PLAYER 1.", True, WHITE),
    )
    WIN = small.render("You Win!", True, WHITE)
    LOSE = small.render("You Lose..", True, WHITE)
    OPPQUIT = vsmall.render("Your Opponent has left", True, WHITE)
    RESIGN = vsmall.render("Your Opponent has resigned", True, WHITE)
    P1WIN = small.render("Player  1   win", True, WHITE)
    P2WIN = small.render("Player  2   win", True, WHITE)
    NO = small.render("NO", True, WHITE)
    OK = small.render("OK", True, WHITE)


class PREF:
    HEAD = large.render("Preferences", True, WHITE)

    SOUNDS = small.render("Sounds", True, WHITE)

    THEMES = small.render("Themes", True, WHITE)

    FONTS = small.render("Fonts", True, WHITE)

    # 주사위 테마
    DICES = small.render("Dices", True, WHITE)
    WHITEDICE = pygame.image.load("res/img/themes_select/white.png")
    REDDICE = pygame.image.load("res/img/themes_select/red.png")
    BLUEDICE = pygame.image.load("res/img/themes_select/blue.png")

    COLON = small.render(":", True, WHITE)

    TRUE = small.render("True", True, WHITE)
    FALSE = small.render("False", True, WHITE)

    BSAVE = medium.render("Save", True, WHITE)

    # 케릭터 선택
    CHARACTOR = small.render("charactor", True, WHITE)
    ICONLISA = pygame.image.load("res/img/charactor/1icon.png")
    ICONBABEL = pygame.image.load("res/img/charactor/2icon.png")
    TXTLISA = small.render("Lisa", True, WHITE)
    TXTBABEL = small.render("Babel", True, WHITE)

    PROMPT = (
        vsmall.render("Are you sure you want to quit?", True, WHITE),
        vsmall.render("Any changes will not be saved.", True, WHITE),
    )

    YES = small.render("YES", True, WHITE)
    NO = small.render("NO", True, WHITE)


class YACHT:     
    # 흰 폰트
    text_title_w = font_obj52.render("Yacht Dice", False, WHITE)
    text_total_w = font_obj18.render("Total", False, WHITE)
    text_ace_w = font_obj16.render("Ace", False, WHITE)
    text_deuces_w = font_obj16.render("Deuces", False, WHITE)
    text_threes_w = font_obj16.render("Threes", False, WHITE)
    text_fours_w = font_obj16.render("Fours", False, WHITE)
    text_fives_w = font_obj16.render("Fives", False, WHITE)
    text_sixes_w = font_obj16.render("Sixes", False, WHITE)
    text_subtotal_w = font_obj18.render("SubTotal", False, WHITE)
    text_choice_w = font_obj16.render("Choice", False, WHITE)
    text_fourofakind_w = font_obj16.render("Quads", False, WHITE)
    text_fullhouse_w = font_obj16.render("F.House", False, WHITE)
    text_sstraight_w = font_obj16.render("S.Strght", False, WHITE)
    text_lstraight_w = font_obj16.render("L.Strght", False, WHITE)
    text_yacht_w = font_obj16.render("Yacht", False, WHITE)
    text_com_w = font_obj24.render("P2", False, WHITE)
    text_player_w = font_obj24.render("P1", False, WHITE)

    PLAYER_w = font_obj24.render("Player", False, WHITE)
    TURN_w = font_obj24.render("Turn", False, WHITE)

    ROLL_w = medium.render("Roll!", True, WHITE)
    LEFT_w = vsmall.render("Left", True, WHITE)

    QUIT_w = medium.render("QUIT", True, WHITE)
    SURREND_w = medium.render("RESIGN", True, WHITE)

    # 검정 폰트
    text_title_b = font_obj52.render("Yacht Dice", False, BLACK)
    text_total_b = font_obj18.render("Total", False, BLACK)
    text_ace_b = font_obj16.render("Ace", False, BLACK)
    text_deuces_b = font_obj16.render("Deuces", False, BLACK)
    text_threes_b = font_obj16.render("Threes", False, BLACK)
    text_fours_b = font_obj16.render("Fours", False, BLACK)
    text_fives_b = font_obj16.render("Fives", False, BLACK)
    text_sixes_b = font_obj16.render("Sixes", False, BLACK)
    text_subtotal_b = font_obj18.render("SubTotal", False, BLACK)
    text_choice_b = font_obj16.render("Choice", False, BLACK)
    text_fourofakind_b = font_obj16.render("Quads", False, BLACK)
    text_fullhouse_b = font_obj16.render("F.House", False, BLACK)
    text_sstraight_b = font_obj16.render("S.Strght", False, BLACK)
    text_lstraight_b = font_obj16.render("L.Strght", False, BLACK)
    text_yacht_b = font_obj16.render("Yacht", False, BLACK)
    text_com_b = font_obj24.render("P2", False, BLACK)
    text_player_b = font_obj24.render("P1", False, BLACK)

    PLAYER_b = font_obj24.render("Player", False, BLACK)
    TURN_b = font_obj24.render("Turn", False, BLACK)

    ROLL_b = medium.render("Roll!", True, BLACK)
    LEFT_b = vsmall.render("Left", True, BLACK)

    QUIT_b = medium.render("QUIT", True, BLACK)
    SURREND_b = medium.render("RESIGN", True, BLACK)

    # 그래픽
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

    ITEM_ONE = pygame.image.load("res/img/one.png")
    ITEM_ODD = pygame.image.load("res/img/odd.png")
    ITEM_EVEN = pygame.image.load("res/img/even.png")

    MINILISA = pygame.image.load("res/img/charactor/1iconsm.png")
    MINIBABEL = pygame.image.load("res/img/charactor/2iconsm.png")
    YES = small.render("YES", True, WHITE)
    NO = small.render("NO", True, WHITE)

    MESSAGE = (
        vsmall.render("Do you want to quit", True, WHITE),
        vsmall.render("this game?", True, WHITE),
    )

class HELP:
    SCORE_BOARD = small.render("Score board", True, RED)
    PLAYER_TURN = small.render("Whos turn", True, RED)
    SAVING_DICES = vsmall.render("click dice to disband", True, RED)
    DICES = vsmall.render("click dice to store", True, RED)
    TO_DO_DICES = vsmall.render("click to roll dices", True, RED)
    
    #scores in game
    ACES = vsmall.render("sum of 1", True, RED)
    TWOS = vsmall.render("sum of 2", True, RED)
    THREE = vsmall.render("sum of 3", True, RED)
    FOURS = vsmall.render("sum of 4", True, RED)
    FIVES = vsmall.render("sum of 5", True, RED)
    SIXES = vsmall.render("sum of 6", True, RED)
    CHOICE = vsmall.render("Any combination", True, RED)
    FOUR_OF_A_KIND = vsmall.render("four dice showing the same face", True, RED)
    F_HOUSE = vsmall.render("Three of one number and two of another", True, RED)
    S_STRAIGHT = vsmall.render("4 dice are in a row", True, RED)
    L_STRAIGHT = vsmall.render("5 dice are in a row", True, RED)
    YACHT = vsmall.render("All dice showing same face", True, RED)
    ODD = vsmall.render("Odd dice", True, RED)
    EVEN = vsmall.render("Even dice", True, RED)
    ONEMORE = vsmall.render("One More", True, RED)

    HELPS = pygame.image.load("res/img/help_s.png")

    PUT_YOUR_IP1 = vsmall.render("Put server ip. if you dont know,", True, RED)
    PUT_YOUR_IP2 = vsmall.render("ask server admin to get IP or domain", True, RED)
    PUT_YOUR_IP3 = vsmall.render("or run server.py to be a server", True, RED)
    CLICK = vsmall.render("click connect button to connect server", True, RED)