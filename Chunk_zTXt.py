from Chunk import Chunk
import zlib


class zTXt(Chunk):
    def __init__(self, keyword=None, compressionMethod=None, compressedText=None):
        self.keyword = keyword
        self.compressionMethod = compressionMethod
        self.compressedText = compressedText

    def __str__(self):
        tmp = self.keyword
        keyword = tmp.decode("utf-8")
        if self.compressionMethod != 0:
            return "Zła wartość metody kompresji"
        if self.compressedText is not None:
            tmp3 = self.compressedText
            compressedText = tmp3.decode("utf-8")
        return "%s : %s " % (keyword, compressedText)

    def chunkzTXt(self, png):
        start = 0
        number = 0
        position = 0
        while position != -1:
            keyword = ""
            text = ""
            position = super(zTXt, self).search(png, start, len(png), b'z', b'T', b'X', b't')

            if position == -1:
                if number == 0:
                    print("Chunk zTXt nie istnieje")
                    return -1
                return 0
            length = super(zTXt, self).lengthChunk(png, position)
            t = position + 4
            index = -1
            for i in range(t, t + length):
                if png[i+1] == b'\x00':
                    index = i + 1
                    break
            tmp = []
            for i in range(t, index):
                a = png[i]
                if len(tmp) == 0:
                    tmp.append(a)
                    keyword = tmp[0]
                else:
                    keyword = b''.join([tmp[0], a])
                    tmp.insert(0, keyword)

            method = int.from_bytes(png[index+1], byteorder='big', signed=True)

            tmp_text = []
            for i in range(index+2, t + length):
                a = png[i]
                if len(tmp_text) == 0:
                    tmp_text.append(a)
                    text = tmp_text[0]
                else:
                    text = b''.join([tmp_text[0], a])
                    tmp_text.insert(0, text)

            decompressText = zlib.decompress(text)
            object = zTXt(keyword, method, decompressText)
            print(object)
            start = position + 4
            number = number + 1
