
def readPNG(filename):
    file = open(filename, 'rb')
    pngRead = []

    while True:
        byte = file.read(1)
        pngRead.append(byte)
        if not byte:
            file.close()
            break
    return pngRead

def checkPNG(png):
    if png[1] == b'P':
        if png[2] == b'N':
            if png[3] == b'G':
                return True
    return False
