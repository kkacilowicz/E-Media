import zlib

from Chunk import Chunk


class IEND(Chunk):
    def chunkIEND(self, png):
        position = super(IEND, self).searchChunk(png, b'I', b'E', b'N', b'D')
        if position == -1:
            print("Plik nie posiada chunk IEND")
            return -1
        else:
            print("Plik posiada chunk IEND")
            tmp = list(png[position - 1])
            if tmp[0] == 0:
                print("Pole danych puste. Strumień danych zakończony prawidłowo")
                return 1
            else:
                print("Pole danych nie jest puste")
                return -1

    def getrawIENDcopy(self, png):
        position = super(IEND, self).searchChunk(png, b'I', b'E', b'N', b'D')
        mylist = []
        # crc is computed with the use of Name + Data of chunk
        checksum = zlib.crc32(png[position])
        # Append all data without crc
        # -5 because -4 (prev crc) and theres alway one ' ' at the end
        for i in range(position - 4, len(png) - 5):
            a = bytes(png[i])
            mylist.append(a)
        for i in range(position+1, len(png) - 5):
            a = bytes(png[i])
            checksum = zlib.crc32(a, checksum)
        checksum = checksum & 0xffffffff
        crc_computed = checksum.to_bytes(4, 'big')
        mylist.append(crc_computed)
        return mylist
