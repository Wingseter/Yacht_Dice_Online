def encode(action, data):
    msg = action 
    for i in range(len(data)):
        msg = msg + str(data[i])
    return msg

def decode(data):
    return data[0:3], int(data[3:])