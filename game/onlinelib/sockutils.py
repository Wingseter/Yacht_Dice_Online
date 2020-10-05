import queue
import socket

q = queue.Queue()

# 정보 수신 쓰레드
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

# 정보 읽어오기
def read():
    return q.get()

# 정보를 읽을수 있는지 검사
def readable():
    return not q.empty()

# 모든 IO 버퍼를 비운다. 
def flush():
    while readable():
        read()

# 정보 쓰기 서버에 전송
def write(sock, msg):
    if msg:
        buffedmsg = msg
        try:
            sock.send(buffedmsg.encode("utf-8"))
        except:
            pass

# 서버로 부터 플레이어들의 목록을 가져온다
def getPlayers(sock):
    write(sock, "pStat")

    msg = read()
    if msg.startswitch("enum"):
        data = []
        for i in range(int(msg[-1])):
            newmsg = read()
            if newmsg == "close":
                return None
            else:
                data.append(newmsg)
        return tuple(data)



