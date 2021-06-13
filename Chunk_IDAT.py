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
            endofchunk = startofchunk + length + 8
            for i in range(startofchunk, endofchunk):
                a = bytes(png[i])
                mylist.append(a)
            checksum = zlib.crc32(png[position])
            for i in range(position + 1, endofchunk):
                a = bytes(png[i])
                checksum = zlib.crc32(a, checksum)
            checksum = checksum & 0xffffffff
            crc_computed = checksum.to_bytes(4, 'big')
            mylist.append(crc_computed)
            start = position + 4


    def getdateIDAT(self, png):
        start = 0
        position = 0
        datelist = []
        while position != -1:
            position = super(IDAT, self).search(png, start, len(png), b'I', b'D', b'A', b'T')
            if position == -1:
                return datelist
            length = super(IDAT, self).lengthChunk(png, position)
            startofchunk = position+4
            endofchunk = startofchunk + length
            datelist_tmp = []
            for i in range(startofchunk, endofchunk):
                a = bytes(png[i])
                datelist_tmp.append(a)
            datelist.append(datelist_tmp)
            start = position + 4

    def getstartIDAT(self, png): # daje miejsce gdzie się chunk IDAT zaczyna
        position = super(IDAT, self).search(png, 0, len(png), b'I', b'D', b'A', b'T')
        assert position != -1, "Chunk IDAT doesn't exist "
        length = super(IDAT, self).lengthChunk(png, position)
        return position - 4, length

    def getendIDAT(self, png): # daje pozycje gdzie się wszystkie chunki IDAT kończą
        start = 0
        position = 0
        endofchunk = 0
        while position != -1:
            position = super(IDAT, self).search(png, start, len(png), b'I', b'D', b'A', b'T')
            if position == -1:
                return endofchunk
            length = super(IDAT, self).lengthChunk(png, position)
            startofchunk = position+4
            endofchunk = startofchunk + length + 4
            start = position + 4