from Chunk import Chunk

class sRGB(Chunk):
    def __init__(self, renderingIntent=None):
        self.renderingIntent = renderingIntent

    def __str__(self):
        if self.renderingIntent == 0:
            return "0 : Perceptual"
        if self.renderingIntent == 1:
            return "1 : Relative colorimetric"
        if self.renderingIntent == 2:
            return "2 : Saturation"
        if self.renderingIntent == 3:
            return "3 : Absolute colorimetric"

        return "Zły odczyt : %d " % (self.renderingIntent)

    def chunksRGB(self, png):
        position = super(sRGB, self).searchChunk(png, b's', b'R', b'G', b'B')
        if position == -1:
            print("Chunk sRGB nie istnieje")
            return -1
        else:
            length = super(sRGB, self).lengthChunk(png, position)
            if length == 1:
                t = position + 4
                a = png[t]
                object = sRGB(int.from_bytes(a, byteorder='big', signed=True))
                print(object)
            else:
                print("Zła długość chunka sRGB")
                return 0