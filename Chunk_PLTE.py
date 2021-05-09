import zlib

from Chunk import Chunk
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np


class PLTE(Chunk):
    def __init__(self, red=None, green=None, blue=None):
        self.r = red
        self.g = green
        self.b = blue

    def __str__(self):
        return " r: %d g: %d b: %d " % (self.r, self.g, self.b)

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
                object = PLTE(a[0], a[1], a[2])
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
            # 8 = 4(length) + 4(name)
            endofchunk = startofchunk + length + 8
            for i in range(startofchunk, endofchunk):
                a = bytes(png[i])
                mylist.append(a)
            # Now program computes crc manually and adds at the end of chunk
            checksum = zlib.crc32(png[position])
            for i in range(position + 1, endofchunk):
                a = bytes(png[i])
                checksum = zlib.crc32(a, checksum)
            checksum = checksum & 0xffffffff
            crc_computed = checksum.to_bytes(4, 'big')
            mylist.append(crc_computed)
            return mylist

    def display(self, listPalette):
        PARAM = 20
        W = 32 * PARAM
        H = 8 * PARAM
        data = np.zeros((H, W, 3), dtype=np.uint8)
        l = 0
        for i in range(0, 8):
            for j in range(i * PARAM, i * PARAM + PARAM):
                index = 32 * i
                for k in range(0, W):
                    object = PLTE()
                    try:
                        object = listPalette[index]
                        data[j][k] = [object.r, object.g, object.b]
                        l = l + 1
                        if l == PARAM and index < len(listPalette):
                            index = index + 1
                            l = 0
                    except:
                        data[j][k] = [255, 255, 255]
        img = Image.fromarray(data, 'RGB')
        img.save("Images/my.png")
        img.show()
