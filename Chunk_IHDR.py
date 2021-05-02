class IHDR:
    def __init__(self, width, heigth, bitDepth, colorType, compressionMethod, filterMethod, interlaceMethod):
        self.width = width
        self.heigth = heigth
        self.bitDepth = bitDepth
        self.colorType = colorType
        self.compressionMethod = compressionMethod
        self.filterMethod = filterMethod
        self.interlaceMethod = interlaceMethod

    def __str__(self):
        return "width: %d \n" \
               "heigth: %d \n" \
               "bitDepth: %d \n" \
               "colorType: %d \n" \
               "compressionMethod: %d \n" \
               "filterMethod %d \n" \
               "interlaceMethod: %d" % (self.width, self.heigth, self.bitDepth, self.colorType, self.compressionMethod, self.filterMethod, self.interlaceMethod)
    def display(self):
        # prawidłowe wartości głębi bitowej to 1,2,4,8,16
        # prawidłowe wartości typu koloru to 0,2,3,4,6. Kody typów kolorów reprezentują sumy następujących
        # wartości: 1 (używana paleta), 2 (użyty kolor) i 4 (używany kanał alfa).
        # dla typu koloru 0 głębia może być 1,2,4,8,16
        # dla typu koloru 2 głębia może być 8,16
        # dla typu koloru 3 głębia może być 1,2,4,8
        # dla typu koloru 4 głębia może być 8, 16
        # dla typu koloru 6 głębia może być 8, 16
        text = f'''Obraz ma wymiary: {self.width} x {self.heigth} pikseli (szerokość x wysokość)
Głębia bitowa wynosi {self.bitDepth}, a typ koloru: {self.colorType}
Metoda kompresji obrazu wynosi : {self.compressionMethod}. Wartość 0 odpowiada wykorzystaniu metody kompresji  deflate/inflate.
Metoda filtracji wynosi {self.filterMethod}. Wartość 0 odpowiada filtrowi adaptacyjnemu z pięcioma podstawowymi typami filtrów
Metoda przeplotu wynosi {self.interlaceMethod}. Wartość 0 mówi że obraz jest bez przeplotu a wartość 1: że wykorzystano przeplot Adam7.'''
        return print(text)
    
def getIHDRChunk(png):
    p = []
    index = 0
    for i in range(0, 40, 4):
        a = png[i]
        b = png[i + 1]
        c = png[i + 2]
        d = png[i + 3]
        e = b''.join([a, b, c, d])
        p.append(e)
        index = index + 1


    if(p[3]==b'IHDR'):
        width = int.from_bytes(p[4], byteorder='big', signed=True)
        heigth = int.from_bytes(p[5], byteorder='big', signed=True)
        tmp = list(p[6])
        bitDepth = tmp[0]
        colorType = tmp[1]
        compressionMethod = tmp[2]
        filterMethod = tmp[3]
        tmp2 = list(p[7])
        interlaceMethod = tmp2[0]
        return IHDR(width, heigth, bitDepth, colorType, compressionMethod, filterMethod, interlaceMethod)
    else:
        return -1

