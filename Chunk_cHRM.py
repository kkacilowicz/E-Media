from Chunk import Chunk


class cHRM(Chunk):
    def __init__(self, WPx=None, WPy=None, Rx=None, Ry=None, Gx=None, Gy=None, Bx=None, By=None):
        self.WPx = WPx
        self.WPy = WPy
        self.Rx = Rx
        self.Ry = Ry
        self.Gx = Gx
        self.Gy = Gy
        self.Bx = Bx
        self.By = By

    def __str__(self):
        return "White Point x : %f \n" \
               "White Point y : %f \n " \
               "Red x : %f \n " \
               "Red y : %f \n" \
               "Green x : %f \n" \
               "Green y : %f \n" \
               "Blue x : %f \n" \
               "Blue x : %f \n" % (self.WPx, self.WPy, self.Rx, self.Ry, self.Gx, self.Gy, self.Bx, self.By)

    def chunkcHRM(self, png):
        position = super(cHRM, self).searchChunk(png, b'c', b'H', b'R', b'M')
        if position == -1:
            print("Chunk cHRM nie istnieje")
            return -1
        else:
            length = super(cHRM, self).lengthChunk(png, position)
            if length == 32:
                t = position + 4
                valuelist = []
                for i in range(t, t + length, 4):
                    a = png[i]
                    b = png[i + 1]
                    c = png[i + 2]
                    d = png[i + 3]
                    e = b''.join([a, b, c, d])
                    valuelist.append(int.from_bytes(e, byteorder='big', signed=True))
                object = cHRM(valuelist[0] * 0.00001,
                              valuelist[1] * 0.00001,
                              valuelist[2] * 0.00001,
                              valuelist[3] * 0.00001,
                              valuelist[4] * 0.00001,
                              valuelist[5] * 0.00001,
                              valuelist[6] * 0.00001,
                              valuelist[7] * 0.00001)
                print(object)
                return object
            else:
                print("Zła długość chunku cHRM")
                return 0
