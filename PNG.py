import read
import Chunk_IHDR

filename = "images4.png"
png = []

png = read.readPNG(filename)
IHDR = Chunk_IHDR.getIHDRChunk(png)
if IHDR == -1:
   print("Chunk IHDR nie istenieje")
else:
   IHDR.display()

