from Chunk import Chunk


class sBIT(Chunk):
    def __init__(self, typeColor=None, byte1=None, byte2=None, byte3=None, byte4=None):
        self.typeColor = typeColor
        self.byte1 = byte1
        self.byte2 = byte2
        self.byte3 = byte3
        self.byte4 = byte4
    def __str__(self):
        if self.typeColor == 0:
            return "Liczba bitów znaczących w danych źródłowych: %d" % (self.byte1)
        if self.typeColor == 2:
            return "Liczby bitów znaczących w kanałach źródłowych: \n" \
                   "kanał czerwony: %d \n" \
                   "kanał zielony: %d \n" \
                   "kanał niebieski: %d \n" % (self.byte1, self.byte2, self.byte3)
        if self.typeColor == 3:
            return "Liczby bitów znaczących w kanałach źródłowych: \n" \
                   "kanał czerwony: %d \n" \
                   "kanał zielony: %d \n" \
                   "kanał niebieski: %d \n" % (self.byte1, self.byte2, self.byte3)
        if self.typeColor == 4:
            return "Liczby bitów znaczących w kanałach źródłowych: \n" \
                   "skala szarości: %d \n" \
                   "alfa: %d \n"  % (self.byte1, self.byte2)
        if self.typeColor == 6:
            return "Liczby bitów znaczących w kanałach źródłowych: \n" \
                   "kanał czerwony: %d \n" \
                   "kanał zielony: %d \n" \
                   "kanał niebieski: %d \n" \
                   "kanał apfa: %d" % (self.byte1, self.byte2, self.byte3, self.byte4)

