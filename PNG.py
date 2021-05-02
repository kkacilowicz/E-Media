import read
import Chunk_IHDR
import Chunk_PLTE
import Chunk_IEND
import Chunk_gAMA
import Chunk
from PIL import Image

filename = "Images/kwiat.png"
png = []
im = Image.open(filename)
# print(im.show())
png = read.readPNG(filename)

IHDR = Chunk_IHDR.getIHDRChunk(png)
if IHDR == -1:
    print("Chunk IHDR nie istenieje")
else:
    IHDR.display()

if IHDR != -1 and IHDR.colorType != 0 and IHDR.colorType != 4:
    plte = Chunk_PLTE.PLTE()
    listPalette = plte.getPLTEChunk(png)
    if listPalette == -1:
        print("Chunk PLTE nie istnieje")
    else:
       # plte.display(listPalette)
        print("CHUNK PLTE OK")
else:
    print("Chunk PLTE nie istnieje")

iend = Chunk_IEND.IEND()
iend.chunkIEND(png)

# print(png)
#chunk = Chunk.Chunk()
#p = chunk.searchChunk(png, b'g', b'A', b'M', b'A')
#print(p)
print(png[30:48])
#l = chunk.lengthChunk(png, p)
#print(l)
gama = Chunk_gAMA.gAMA()
print("bitDepth", IHDR.bitDepth)
gama.chunkgAMA(png, IHDR.bitDepth)
