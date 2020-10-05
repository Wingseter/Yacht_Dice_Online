from game.onlinelib import *
import threading

VERSION = "1.0"
def main(win, addr):
    if addr is None:
        return 
    
    # 연결 로딩 창
    showLoading(win)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    addr = "192.168.0.200"

    try:
        sock.connect((addr, 9090))
    except:
        showLoading(win, 0)
        return
    
    # 서버 통신 쓰레드 생성
    thread = threading.Thread(target=bgThread, args=(sock,))
    thread.start()

    # 서버에 클라이언트의 버전 전송
    write(sock, VERSION)

    # 서버에서 정보 수신
    msg = read()
    print(msg)
    if msg == "errVer":
        showLoading(win, 1)

    elif msg == "errBusy":
        showLoading(win, 2)
    
    elif msg == "errLock":
        showLoading(win, 3)
    
    elif msg.startswith("GTag"):
        lobby(win, sock, int(msg[4:]))

    sock.close()
    thread.join()
    flush()
    


    