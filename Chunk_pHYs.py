from Chunk import Chunk


class pHYs(Chunk):
    def __init__(self, ppuX=None, ppuY=None, us=None):
        self.pixelPerUnitX = ppuX
        self.pixelPerUnitY = ppuY
        self.unitSpecifier = us

    def __str__(self):
        return "pixel per unit X: %d \n" \
               "pixel per unit Y: %d \n" \
               "Unit specifier: %d" % (self.pixelPerUnitX, self.pixelPerUnitY, self.unitSpecifier)

    def chunkpHYs(self, png):
        position = super(pHYs, self).searchChunk(png, b'p', b'H', b'Y', b's')
        if position == -1:
            print("Chunk pHYs nie istnieje")
            return -1
        else:
            length = super(pHYs, self).lengthChunk(png, position)
            if length == 9:
                t = position + 4
                valuelist = []
                for i in range(t, t + length - 1, 4):
                    a = png[i]
                    b = png[i + 1]
                    c = png[i + 2]
                    d = png[i + 3]
                    e = b''.join([a, b, c, d])
                    valuelist.append(int.from_bytes(e, byteorder='big', signed=True))
                valuelist.append(int.from_bytes(png[t + length - 1], byteorder='big', signed=True))
                object = pHYs(valuelist[0], valuelist[1], valuelist[2])
                if object.unitSpecifier == 0 or object.unitSpecifier == 1:
                    print(object)
                    return object
                else:
                    print("Zła wartość unit specifier")
                    return 0
            else:
                print("Zła długość chunku pHYs")
                return 0
