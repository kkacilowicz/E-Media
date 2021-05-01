import read
import Chunk_IHDR
import Chunk_PLTE
import Chunk_IEND
from PIL import Image

filename = "kwiat.png"
png = []
im = Image.open(filename)
#print(im.show())
png = read.readPNG(filename)


IHDR = Chunk_IHDR.getIHDRChunk(png)
if IHDR == -1:
   print("Chunk IHDR nie istenieje")
else:
   IHDR.display()


if IHDR != -1 and IHDR.colorType != 0 and IHDR.colorType !=4:
   listPalette = Chunk_PLTE.getPLTEChunk(png)
   if listPalette == -1:
      print("Chunk PLTE nie istnieje")
   else:
      #Chunk_PLTE.display(listPalette)
      print("CHUNK PLTE OK")
else:
   print("Chunk PLTE nie istnieje")


Chunk_IEND.chunkIEND(png)

#print(png)