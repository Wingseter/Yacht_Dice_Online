from game.onlinelib import *
import threading

def main(win, addr):
    if addr is None:
        return 

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    addr = "192.168.0.200"

    try:
        sock.connect((addr, 9090))
    except:
        showLoading(win, 0)
        return
    
    write(sock, "HELLO")
    showLoading(win,1)
    msg = read()

    sock.close()
    


    