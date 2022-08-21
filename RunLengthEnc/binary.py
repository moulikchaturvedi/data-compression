#code to convert any message to binary format

def to_binary(message):
    binary = ''
    while message > 0:
        binary = str(message % 2) + binary
        message = message // 2

    if len(binary) < 4:
        binary = '0' * (4 - len(binary)) + binary

    return binary