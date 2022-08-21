message= '0000011100'

count = 0
for x in message:
    if x == '0':
        count += 1
    else:
        # return count
        print (str(count) + '  ' + message[count::])
        break