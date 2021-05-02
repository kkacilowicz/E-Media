from Chunk import Chunk
import zlib

class IDAT(Chunk):

    def chunkIDAT(self, png):
        start = 0
        number = 0
        position = 0
        listIDAT = []
        while position != 1:
            position = super(IDAT, self).search(png, start, len(png), b'I', b'D', b'A', b'T')
            if position == -1:
                if number == 0:
                    print("Chunk tEXt nie istnieje")
                    return -1
                print(listIDAT)
                return 0
            length = super(IDAT, self).lengthChunk(png, position)
            t = position + 4
            score = []
            tmp = []
            for i in range(t, t+length):
                a = png[i]
                score.append(a)
                #if len(tmp) == 0:
                #    tmp.append(a)
                #    score = tmp[0]
                #else:
                    #score = b''.join([tmp[0], a])
                    #tmp.insert(0, score)
            #x = int.from_bytes(score, byteorder='big', signed=True)
            x = zlib.decompress(score[0], 0)
            listIDAT.append(x)
            start = position + 4
            number = number + 1


