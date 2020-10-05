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
                if 450 < x < 480 and 120 < y < 150:
                    playerList = getPlayers(sock)
                    if playerList is None:
                        return
                    showLobby(win, key, playerList)
                    
                if 30 < x < 1100:
                    for i in range(len(playerList)):
                        if 172 + 30 * i < y < 208 + 30 * i:
                            write(sock, "rg" + playerList[i][:4])
                            newMsg = read()
                            if newMsg == "msgOk":
                                stat = request(win, None, sock)
                                if stat is None:
                                    return
                                elif stat and yacht(win, sock, 0):
                                    return

                            playerList = getPlayers(sock)
                            if playerList is None:
                                return
                            showLobby(win, key, playerList)
                            
        if readable():
            msg = read()
            
            if msg == "close":
                return

            elif msg.startswith("gr"):
                if request(win, msg[2:]):
                    write(sock, "gmOk" + msg[2:])
                    if yacht(win, sock, 1):
                        return
                    else:
                        playerList = getPlayers(sock)
                        if playerList is None:
                            return
                        showLobby(win, key, playerList)
                else:
                    write(sock, "gmNo" + msg[2:])
                    showLobby(win, key, playerList)

def yacht(win, sock, player):
    pass
                