b=bytes([10,20,30,40])
#b[3] = 400   #TypeError:
ba=bytearray([10,20,30,40])
ba[3] = 255

for element in ba:
    print(element)