from Chunk import Chunk
import zlib


class IDAT(Chunk):

    def chunkIDAT(self, png):
        start = 0
        number = 0
        position = 0
        listIDAT = []
        while position != -1:
            position = super(IDAT, self).search(png, start, len(png), b'I', b'D', b'A', b'T')
            if position == -1:
                if number == 0:
                    print("Chunk IDAT nie istnieje")
                    return -1
                # print(listIDAT)
                return number
            length = super(IDAT, self).lengthChunk(png, position)
            t = position + 4
            score = []
            tmp = []
            for i in range(t, t + length):
                a = png[i]
                if len(tmp) == 0:
                    tmp.append(a)
                    score = tmp[0]
                else:
                    score = b''.join([tmp[0], a])
                    tmp.insert(0, score)
            # x = zlib.decompress(score)
            listIDAT.append(score)
            start = position + 4
            number = number + 1

    def getrawIDATscopy(self, png):
        start = 0
        position = 0
        mylist = []
        while position != -1:
            position = super(IDAT, self).search(png, start, len(png), b'I', b'D', b'A', b'T')
            if position == -1:
                # print(listIDAT)
                return mylist
            length = super(IDAT, self).lengthChunk(png, position)
            tmp = []
            startofchunk = position - 4
            endofchunk = startofchunk + length + 12
            for i in range(startofchunk, endofchunk):
                a = bytes(png[i])
                mylist.append(a)
            start = position + 4

