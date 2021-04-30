import read
import Chunk_IHDR

filename = "images4.png"
png = []

png = read.readPNG(filename)
'''
IHDR = Chunk_IHDR.getIHDRChunk(png)
if IHDR == -1:
   print("Chunk IHDR nie istenieje")
else:
   IHDR.display()
'''


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


print(searchPLTE(png))

print()
