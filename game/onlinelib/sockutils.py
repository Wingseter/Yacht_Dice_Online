import queue
import socket

q = queue.Queue()

def read():
    return q.get()

def write(sock, msg):
    if msg:
        buffedmsg = msg
        try:
            sock.send(buffedmsg.encode("utf-8"))
        except:
            pass



