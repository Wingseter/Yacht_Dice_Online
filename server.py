import random
import socket
import threading
import time
import urllib.request import urlopen

VERSION = "v1.0"
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

player = []
busyPpl = set()
lock = False
total = 0

def read(sock, timeout = None):
    try: 
        msg = sock.recv(8).decode("utf-8")
        print(msg)
    except:
        pass

# 플레이어 가 접속 해제되었을때 호출
def onQuit(sock, key):
    write(sock, "close")
    rmKey(key)
    rmBusy(key)
    sock.close() 

# 플레이어와 서버 게임의 통신 관리
def player(sock, key):
    try:
        while True:
            msg = read(sock)

            if msg == "quit":
                onQuit(sock, key)
                return
    except Exception as e:
        print("서버: 플레이에 에러 발생")
        print("서버: ", e)
        onQuit(sock, key)
          
while True:
    try:
        newSock, _ = mainSock.accept()
    except:
        print("서버: 소켓 생성 오류")
        break

    total += 1
    print("서버: 클라이언트가 연결 시도중입니다.")
    read(newSock)