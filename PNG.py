import read
import Chunk_IHDR

filename = "kwiat.png"
png = []

png = read.readPNG(filename)
IHDR = Chunk_IHDR.getIHDRChunk(png)
IHDR.display()