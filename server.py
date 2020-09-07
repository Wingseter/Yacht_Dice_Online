import socket

mainSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mainSock.bind(("0.0.0.0", 9090))
mainSock.listen(16)

print("SERVER IS STARTING")

def read(sock, timeout = None):
    try: 
        msg = sock.recv(8).decode("utf-8")
        print(msg)
    except:
        pass
    

while True:
    try:
        newSock, _ = mainSock.accept()
    except:
        print("Connection Error")
        break

    read(newSock)