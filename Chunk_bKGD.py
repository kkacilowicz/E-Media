from Chunk import Chunk


class bKGD(Chunk):
    def __init__(self, typeColor=None, value1=None, value2=None, value3=None):
        self.typeColor = typeColor
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3

    def __str__(self):
        if self.typeColor == 3:
            return "Palette index: %d" % self.value1
        if self.typeColor == 0 or self.typeColor == 4:
            return "Gray: %d " % self.value1
        if self.typeColor == 2 or self.typeColor == 6:
            return "Red : %d \n" \
                   "Green : %d \n" \
                   "Blue: %d " % (self.value1, self.value2, self.value3)
        return " Zła wartość typu koloru "

    def chunkbKGD(self, png, typeColor):
        position = super(bKGD, self).searchChunk(png, b'b', b'K', b'G', b'D')
        if position == -1:
            print("Chunk bKGD nie istnieje")
            return -1
        else:
            length = super(bKGD, self).lengthChunk(png, position)
            if (typeColor == 2 and length == 6) or (typeColor == 6 and length == 6):
                listValue = []
                t = position + 4
                for i in range(t, t+length, 2):
                    a = png[i]
                    b = png[i+1]
                    c = png[i+2]
                    e = b''.join([a, b, c])
                    listValue.append(int.from_bytes(e, byteorder='big', signed=True))
                object = bKGD(typeColor, listValue[0], listValue[1], listValue[2])
                print(object)
                return object
            if (typeColor == 0 and length == 2) or (typeColor == 4 and length == 2):
                t = position + 4
                a = png[t]
                b = png[t+1]
                c = b''.join([a, b])
                object = bKGD(typeColor, (int.from_bytes(c, byteorder='big', signed=True)))
                print(object)
                return object
            if typeColor == 3 and length == 1:
                t = position + 4
                a = png[t]
                object = bKGD(typeColor, (int.from_bytes(a, byteorder='big', signed=True)))
                print(object)
                return object
            else:
                print("Zła długość chunku bKGD")
                return 0