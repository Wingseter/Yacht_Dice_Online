import queue
import socket

q = queue.Queue()

def bgThread(sock):
    try:
        while True:
            msg = sock.recv(8).decode("utf-8")

            if not msg:
                if q.empty():
                    q.put("close")
                return
            if "X" not in msg:
                q.put(msg.strip())
    except:
        if q.empty():
            q.put("close")
            
def read():
    return q.get()

def write(sock, msg):
    if msg:
        buffedmsg = msg
        try:
            sock.send(buffedmsg.encode("utf-8"))
        except:
            pass



