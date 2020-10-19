def encode(action, data):
    data = action + str(data)
    return data

def decode(data):
    return data[:4], int(data[4:])