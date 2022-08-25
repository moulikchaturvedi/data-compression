#code to convert any message to binary format in context for 4 bit binary RLE

def to_binary(message):
    binary = ''
    binary15 = '1111'

    if int(message) >= 15:
        message = message - 15
        binary = binary15 + to_binary(message)

    while int(message) > 0:
        binary = str(message % 2) + binary
        message = message // 2

    if len(binary) < 4:
        binary = '0' * (4 - len(binary)) + binary

    return binary