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
        for i in range(position - 4, len(png)):
            a = bytes(png[i])
            mylist.append(a)
        return mylist
