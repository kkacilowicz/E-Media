import read
import Chunk_IHDR
import Chunk_PLTE
import Chunk_IEND
import Chunk_gAMA
import Chunk_cHRM
import Chunk_sRGB
import Chunk_pHYs
import Chunk_sBIT

#from PIL import Image

filename = "Images/gora.png"
png = []
#im = Image.open(filename)
# print(im.show())
png = read.readPNG(filename)



# IHDR ********************************************************************************************

IHDR = Chunk_IHDR.getIHDRChunk(png)
if IHDR == -1:
    print("Chunk IHDR nie istenieje")
else:
    IHDR.display()

# PLTE ********************************************************************************************
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

# IEND ********************************************************************************************
iend = Chunk_IEND.IEND()
iend.chunkIEND(png)

# gAMA ********************************************************************************************
gama = Chunk_gAMA.gAMA()
gama.chunkgAMA(png)

# cHRM ********************************************************************************************
chrm = Chunk_cHRM.cHRM()
chrm.chunkcHRM(png)

# sRGB ********************************************************************************************
srgb = Chunk_sRGB.sRGB()
srgb.chunksRGB(png)

# pHYs ********************************************************************************************
phys = Chunk_pHYs.pHYs()
phys.chunkpHYs(png)

# sBIT ********************************************************************************************
sbit = Chunk_sBIT.sBIT()
if IHDR == -1:
    print("Chunk sBIT nie może być odczytany bo nie ma chunku IHDR")
else:
    sbit.chunksBIT(png, IHDR.colorType)