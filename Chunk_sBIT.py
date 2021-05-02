from Chunk import Chunk


class sBIT(Chunk):
    def __init__(self, typeColor=None, byte1=None, byte2=None, byte3=None, byte4=None):
        self.typeColor = typeColor
        self.byte1 = byte1
        self.byte2 = byte2
        self.byte3 = byte3
        self.byte4 = byte4
    def __str__(self):
        if self.typeColor == 0:
            return "Liczba bitów znaczących w danych źródłowych: %d" % (self.byte1)
        if self.typeColor == 2:
            return "Liczby bitów znaczących w kanałach źródłowych: \n" \
                   "kanał czerwony: %d \n" \
                   "kanał zielony: %d \n" \
                   "kanał niebieski: %d \n" % (self.byte1, self.byte2, self.byte3)
        if self.typeColor == 3:
            return "Liczby bitów znaczących w kanałach źródłowych: \n" \
                   "kanał czerwony: %d \n" \
                   "kanał zielony: %d \n" \
                   "kanał niebieski: %d \n" % (self.byte1, self.byte2, self.byte3)
        if self.typeColor == 4:
            return "Liczby bitów znaczących w kanałach źródłowych: \n" \
                   "skala szarości: %d \n" \
                   "alfa: %d \n"  % (self.byte1, self.byte2)
        if self.typeColor == 6:
            return "Liczby bitów znaczących w kanałach źródłowych: \n" \
                   "kanał czerwony: %d \n" \
                   "kanał zielony: %d \n" \
                   "kanał niebieski: %d \n" \
                   "kanał apfa: %d" % (self.byte1, self.byte2, self.byte3, self.byte4)

    def chunksBIT(self, png, typeColor):
        position = super(sBIT, self).searchChunk(png, b's', b'B', b'I', b'T')
        if position == -1:
            print("Chunk sBIT nie istnieje")
            return -1
        else:
            length = super(sBIT, self).lengthChunk(png, position)
            if length == 1 and typeColor == 0:
                t = position + 4
                a = png[t]
                object = sBIT(int.from_bytes(a, byteorder='big', signed=True))
                print(object)
                return object
            if length == 3 and typeColor == 2:
                t = position + 4
                a = png[t]
                b = png[t + 1]
                c = png[t + 2]
                d = b''.join([a, b, c])
                value = list(d)
                object = sBIT(typeColor, value[0], value[1], value[2])
                print(object)
                return object
            if length == 3 and typeColor == 3:
                t = position + 4
                a = png[t]
                b = png[t + 1]
                c = png[t + 2]
                d = b''.join([a, b, c])
                value = list(d)
                object = sBIT(typeColor, value[0], value[1], value[2])
                print(object)
                return object
            if length == 2 and typeColor == 4:
                t = position + 4
                a = png[t]
                b = png[t + 1]
                d = b''.join([a, b])
                value = list(d)
                object = sBIT(typeColor, value[0], value[1])
                print(object)
                return object
            if length == 4 and typeColor == 6:
                t = position + 4
                a = png[t]
                b = png[t + 1]
                c = png[t + 2]
                d = png[t + 3]
                e = b''.join([a, b, c, d])
                value = list(e)
                object = sBIT(typeColor, value[0], value[1], value[2], value[3])
                print(object)
                return object
            print("Zła długość chunku sBIT")
            return 0
