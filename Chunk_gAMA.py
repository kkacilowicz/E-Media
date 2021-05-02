from Chunk import Chunk


class gAMA(Chunk):

    def chunkgAMA(self, png, bitDepth):
        position = super(gAMA, self).searchChunk(png, b'g', b'A', b'M', b'A')
        if position == -1:
            print("Chunk gAMA nie istnieje")
            return -1
        else:
            length = super(gAMA, self).lengthChunk(png, position)
            if length == 4:
                t = position + 4
                a = png[t]
                b = png[t + 1]
                c = png[t + 2]
                d = png[t + 3]
                d = b''.join([a, b, c, d])
                read = int.from_bytes(d, byteorder='big', signed=True)
                gamma = round(read * 0.00001, 5)
                print("Wartość gamma wynosi: ", gamma)
                return gamma
            else:
                print("Zła długość chunka gAMA")
                return 0
