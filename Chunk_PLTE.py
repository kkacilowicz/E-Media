from Chunk import Chunk


class PLTE(Chunk):
    def __init__(self, paletteEntries=None, red=None, green=None, blue=None):
        self.paletteEntries = paletteEntries
        self.r = red
        self.g = green
        self.b = blue

    def __str__(self):
        return "pallete entries: %d r: %d g: %d b: %d " % (self.paletteEntries, self.r, self.g, self.b)

    def getThreeBytesSeries(self, position, png, length):
        if length % 3 == 0:
            tmp = length // 3
            if 257 > tmp > 1:
                threeBytesSeries = []
                t = position + 4  # pierwszy bajt po nazwie
                for i in range(t, t + length, 3):
                    a = png[i]
                    b = png[i + 1]
                    c = png[i + 2]
                    d = b''.join([a, b, c])
                    threeBytesSeries.append(d)
                return threeBytesSeries
            else:
                return -1
        else:
            return -1

    def getPLTEChunk(self, png):
        position = super(PLTE, self).searchChunk(png, b'P', b'L', b'T', b'E')
        if position == -1:
            return -1
        else:
            length = super(PLTE, self).lengthChunk(png, position)
            listThreeBytesSeries = self.getThreeBytesSeries(position, png, length)
            listPalette = []
            l = len(listThreeBytesSeries)
            for i in range(0, l):
                a = list(listThreeBytesSeries[i])
                object = PLTE(i + 1, a[0], a[1], a[2])
                listPalette.append(object)
            return listPalette

    def getrawPLTEdata(self, png):
        position = super(PLTE, self).searchChunk(png, b'P', b'L', b'T', b'E')
        mylist = []
        if position == -1:
            return -1
        else:
            length = super(PLTE, self).lengthChunk(png, position)
            startofchunk = position - 4
            # 12 = 4(length) + 4(name) + 4(crc)
            endofchunk = startofchunk + length + 12
            for i in range(startofchunk, endofchunk):
                a = bytes(png[i])
                mylist.append(a)
            return mylist

    def display(self, listPalette):
        for i in listPalette:
            print(i)
