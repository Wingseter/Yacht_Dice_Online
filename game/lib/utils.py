def encode(action, data):
    msg = action 
    for i in range(len(data)):
        msg = msg + str(data[i])
    return msg

def decode(data):
    return data[0:3], data[3:]


def truefalse(input):
    if input == 1:
        return True
    else:
        return False