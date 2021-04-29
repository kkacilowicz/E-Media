
def readPNG(filename):
    file = open(filename, 'rb')
    pngRead = []

    while True:
        byte = file.read(4)
        pngRead.append(byte)
        if not byte:
            file.close()
            break
    return pngRead

#print("szerokosc" + str(int.from_bytes(a,byteorder='big' , signed=True)))
#print("wysokosc" + str(int.from_bytes(b,byteorder='big' , signed=True)))
#print(int.from_bytes(c,byteorder='big' , signed=True))
#print(int.from_bytes(d,byteorder='big' , signed=True))