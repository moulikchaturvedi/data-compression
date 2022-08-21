#code to convert any message to binary format

def to_binary(message):
    binary = ''
    while message > 0:
        binary = str(message % 2) + binary
        message = message // 2
    return binary

print (to_binary(10))