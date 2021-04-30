class PLTE:
    def __init__(self, palleteEntries, red, green, blue):
        self.palleteEntries = palleteEntries
        self.r = red
        self.g = green
        self.b = blue
    def __str__(self):
        return "pallete entries: %d r: %d g: %d b: %d " % (self.palleteEntries, self.r, self.g, self.b)



def searchPLTE(png):
    length = len(png)
    position = 0
    for i in range(0, length):
        if png[i] == b'P':
            if png[i + 1] == b'L':
                if png[i + 2] == b'T':
                    if png[i + 3] == b'E':
                        position = i
                        break
    return position

def lengthPLTE(png, position):
   a = png[position-4]
   b = png[position-3]
   c = png[position-2]
   d = png[position-1]
   e = b''.join([a, b, c, d])
   length = int.from_bytes(e, byteorder='big', signed=True)
   if length % 3 == 0:
      tmp = length // 3
      if tmp < 257 and tmp > 1:
         return length
      else:
         return -1
   return -1  # nieprawidlowa dlugosc



def getThreeBytesSeries(position, png, length):
   threeBytesSeries = []
   t = position + 4 # pierwszy bajt po nazwie
   for i in range(t, t+length, 3):
      a = png[i]
      b = png[i+1]
      c = png[i+2]
      d = b''.join([a, b, c])
      threeBytesSeries.append(d)
   return threeBytesSeries

def getPLTEChunk(png):
    position = searchPLTE(png)
    if position == 0:
        return -1
    else:
        length = lengthPLTE(png, position)
        listThreeBytesSeries = getThreeBytesSeries(position, png, length)
        listPalette = []
        l = len(listThreeBytesSeries)
        for i in range(0, l):
            a = list(listThreeBytesSeries[i])
            object = PLTE(i+1, a[0], a[1], a[2])
            listPalette.append(object)
        return listPalette

def display(listPalette):
    for i in listPalette:
        print(i)


