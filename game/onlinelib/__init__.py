from game.onlinelib.utils import *

def lobby(win, sock, key, LOAD):
    clock = pygame.time.Clock()

    playerList = getPlayer(sock)
    if playerList is None:
        return
    
    while True:
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                write(sock, "quit")
                return
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # 새로고침 했을때
                if True:
                    playerList = getPlayer(sock)
                    if playerList is None:
                        return