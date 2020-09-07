from game.onlinelib.sockutils import *

def main(win, addr):
    if addr is None:
        return 

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    addr = "192.168.0.200"

    try:
        sock.connect((addr, 9090))
    except:
        print("Cant Connect Server")
        return
    
    write(sock, "HELLO")
    msg = read()

    sock.close()
    


    