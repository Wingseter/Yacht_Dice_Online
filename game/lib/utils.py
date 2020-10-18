def encode(fro, to, ):
    data = LETTER[fro[0]] + str(9 - fro[1]) + LETTER[to[0]] + str(9 - to[1])

    return data

def decode(data):
    if len(data) == 4:
        return (
            [LETTER.index(data[0]), 9 - int(data[1])],
            [LETTER.index(data[2]), 9 - int(data[3])],
            None,
        )
    elif len(data) == 5:
        return (
            [LETTER.index(data[0]), 9 - int(data[1])],
            [LETTER.index(data[2]), 9 - int(data[3])],
            data[4],
        )