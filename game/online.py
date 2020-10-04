from game.onlinelib import *
import threading

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

    
    write(sock, "HELLO")
    showLoading(win,1)
    msg = read()

    sock.close()
    


    