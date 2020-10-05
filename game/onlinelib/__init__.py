from game.onlinelib.utils import *
def lobby(win, sock, key):
    clock = pygame.time.Clock()

    playerList = getPlayers(sock)
    if playerList is None:
        return
    showLobby(win, key, playerList)

    while True:
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                write(sock, "quit")
                return
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # 새로고침 했을때
                if 270 < x < 300 and 85 < y < 115:
                    playerList = getPlayers(sock)
                    if playerList is None:
                        return
                    showLobby(win, key, playerList)
               