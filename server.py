import random
import socket
import threading
import time
from urllib.request import urlopen

VERSION = "1.0"
START_TIME = time.perf_counter()

print("서버 시작중 잠시만 기다려 주세요.....")
mainSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mainSock.bind(("0.0.0.0", 9090))
mainSock.listen(16)
print("서버: 서버가 성공적으로 시작되었습니다.")
print("서버: 연결 포트 9090.")

# 서버의 IP 결정
IP = socket.gethostbyname(socket.gethostname())
# 네트워크 연결 확인
if IP == "127.0.0.1":
    print("서버: 서버가 네트워크에 연결되지 않았습니다.")
else:
    print("서버: 서버의 IP 주소는: ", IP)

def getTime():
    sec = round(time.perf_counter() - START_TIME)
    minutes, sec = divmod(sec, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return f"{days} days, {hours} hours, {minutes} minutes, {sec} seconds"

players = []
busyPpl = set()
lock = False
total = 0

def read(sock, timeout = None):
    try: 
        msg = sock.recv(8).decode("utf-8")
        if "X" in msg:
            return read(sock, timeout)
        
        if msg:
            return msg.strip()
    except:
        pass
    return "quit"

# 패킷 손실 발생 했을때
def send_error_buffer(sock, bufsize):
    sent = sock.send(("X" * bufsize).encode("utf-8"))
    if sent < bufsize:
    
        send_error_buffer(sock, bufsize - sent)

# 패킷 쓰기
def write(sock, msg):
    if msg:
        buffedmsg = msg + (" " * (8 - len(msg)))
        try:
            sent = sock.send(buffedmsg.encode("utf-8"))
            if sent < 8:
                send_error_buffer(sock, 8 - sent)
                write(sock, msg)
        except:
            pass

# Key로 플레이어 알아내기
def getByKey(key):
    for player in players:
        if player[1] == int(key):
            return player[0]

# 플레이어키 삭제
def rmKey(key):
    global players
    players.remove((getByKey(key), key))

# 플레이어 바쁜것 삭제
def mkBusy(*keys):
    global busyPpl
    for key in keys:
        busyPpl.add(int(key))

# 플레이어 게임중인것 삭제
def rmBusy(*keys):
    global busyPpl
    for key in keys:
        busyPpl.discard(int(key))


# 두개의 클라이언트 간의 통신
def game(sock1, sock2):
    while True:
        msg = read(sock1)
        write(sock2, msg)
        if msg == "quit":
            return True

        elif msg in ["resign", "end"]:
            return False

# 플레이어 가 접속 해제되었을때 호출
def onQuit(sock, key):
    write(sock, "close")
    rmKey(key)
    sock.close() 

# 플레이어와 서버 게임의 통신 관리
def player(sock, key):
    try:
        while True:
            msg = read(sock)

            if msg == "quit":
                onQuit(sock, key)
                return
            elif msg == "pStat":
                print(f"플레이어 {key}: 플레이어들의 상태를 요청했습니다.")
                data = list(zip(*players))[1], list(busyPpl)
                if len(data[0]) - 1 in range(10):
                    write(sock, "enum" + str(len(data[0]) -1))

                for i in data[0]:
                    if i != key:
                        if i in data[1]:
                            write(sock, str(i) + "b")
                        else:
                            write(sock, str(i) + "a")
            elif msg.startswith("rg"):
                print(f"플레이어{key}: 플레이어{msg[2:]} 에게 게임 요청했습니다.")
                oSock = getByKey(msg[2:])
                if oSock is not None:
                    if int(msg[2:]) not in busyPpl:
                        mkBusy(key, msg[2:])
                        write(sock, "msgOk")
                        write(oSock, "gr" + str(key))
                        newMsg = read(sock)
                        if newMsg == "ready":
                            print(f"서버: 플레이어{key} 게임 시작")
                            if game(sock, oSock):
                                onQuit(sock, key)
                                return
                            else:
                                rmBusy(key)
                                print(f"서버: 플레이어{key} 게임 끝")

                        elif newMsg == "quit":
                            onQuit(sock, key)
                            write(oSock, "quit")
                            return

                    else:
                        print(f"서버: 플레이어{key}가 바쁜 플레이어에게 요청을 보냈습니다.")
                        write(sock, "errPBusy")
                else:
                    print(f"서버: 플레이어{key} 불가능한 키를 보냈습니다.")
                    write(sock, "errKey")

            elif msg.startswith("gmOk"):
                print(f"플레이어{key}: 플레이어{msg[4:]}의 요청을 수락했습니다.")
                oSock = getByKey(msg[4:])
                write(oSock, "start")
                print(f"서버: 플레이어{key} 게임에 들어갔습니다.")
                if game(sock, oSock):
                    onQuit(sock, key)
                    return
                else:
                    rmBusy(key)
                    print(f"서버: 플레이어{key} 게임을 마쳤습니다.")

            elif msg.startswith("gmNo"):
                print(f"플레이어{key}: 플레이어{msg[4:]}의 요청을 거부했습니다.")
                oSock = getByKey(msg[4:])
                write(oSock, "nostart")
                rmBusy(key, msg[4:])

    except Exception as e:
        print("서버: 플레이에 에러 발생")
        print("서버: ", e)
        onQuit(sock, key)

# 중복되지 않는 게임 태그 생성
def genKey():
    key = random.randint(1000, 9999)
    for player in players:
        if player[1] == key:
            return genKey()
    return key
      
while True:
    try:
        newSock, _ = mainSock.accept()
    except:
        print("서버: 소켓 생성 오류")
        break

    total += 1
    print("서버: 클라이언트가 연결 시도중입니다.")
    if read(newSock, 3) == VERSION:
        if len(players) < 10:
            if not lock:
                key = genKey()
                players.append((newSock, key))
                print(f"서버: 성공적으로 연결되었습니다. 게임테그 - {key}")
                write(newSock, "GTag" + str(key))
                threading.Thread(target=player, args=(newSock, key)).start()
            else:
                print("서버: 서버가 잠겼습니다. 연결을 거부합니다")
                write(newSock, "errLock")
                newSock.close()
        else:
            print("서버: 서버가 바쁩니다. 연결을 거부합니다")
            write(newSock, "errLock")
            newSock.close()
    else:
        print("서버: 버전이 맞지 않습니다. 연결을 거부합니다")
        write(newSock, "errVer")
        newSock.close()
