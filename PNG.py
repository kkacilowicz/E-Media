import read
import Chunk_IHDR
import Chunk_PLTE
import Chunk_IEND
import Chunk_gAMA
import Chunk_cHRM
import Chunk_sRGB
import Chunk_pHYs
import Chunk_sBIT
import Chunk_tEXt
import Chunk_bKGD
import Chunk_IDAT
import Chunk
#from PIL import Image

filename = "Images/images.png"
png = []
#im = Image.open(filename)
# print(im.show())
png = read.readPNG(filename)

if read.checkPNG(png):

    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("                                          PNG                                              ")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    # IHDR ********************************************************************************************
    print()
    print("++++++++++++++++                  CHUNK IHDR                               ++++++++++++++++")
    print()
    IHDR = Chunk_IHDR.getIHDRChunk(png)
    if IHDR == -1:
        print("Chunk IHDR nie istenieje")
    else:
        IHDR.display()

    # PLTE ********************************************************************************************
    print("-------------------------------------------------------------------------------------------")
    print("++++++++++++++++                  CHUNK PLTE                               ++++++++++++++++")
    print()
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
    print("-------------------------------------------------------------------------------------------")
    print("++++++++++++++++                  CHUNK IEND                               ++++++++++++++++")
    print()
    iend = Chunk_IEND.IEND()
    iend.chunkIEND(png)

    # gAMA ********************************************************************************************
    print("-------------------------------------------------------------------------------------------")
    print("++++++++++++++++                  CHUNK gAMA                               ++++++++++++++++")
    print()
    gama = Chunk_gAMA.gAMA()
    gama.chunkgAMA(png)

    # cHRM ********************************************************************************************
    print("-------------------------------------------------------------------------------------------")
    print("++++++++++++++++                  CHUNK cHRM                               ++++++++++++++++")
    print()
    chrm = Chunk_cHRM.cHRM()
    chrm.chunkcHRM(png)

    # sRGB ********************************************************************************************
    print("-------------------------------------------------------------------------------------------")
    print("++++++++++++++++                  CHUNK sRGB                               ++++++++++++++++")
    print()
    srgb = Chunk_sRGB.sRGB()
    srgb.chunksRGB(png)

    # pHYs ********************************************************************************************
    print("-------------------------------------------------------------------------------------------")
    print("++++++++++++++++                  CHUNK pHYs                               ++++++++++++++++")
    print()
    phys = Chunk_pHYs.pHYs()
    phys.chunkpHYs(png)

    # sBIT ********************************************************************************************
    print("-------------------------------------------------------------------------------------------")
    print("++++++++++++++++                  CHUNK sBIT                               ++++++++++++++++")
    print()
    sbit = Chunk_sBIT.sBIT()
    if IHDR == -1:
        print("Chunk sBIT nie może być odczytany bo nie ma chunku IHDR")
    else:
        sbit.chunksBIT(png, IHDR.colorType)

    # tEXt ********************************************************************************************
    print("-------------------------------------------------------------------------------------------")
    print("++++++++++++++++                  CHUNK tEXt                               ++++++++++++++++")
    print()
    text = Chunk_tEXt.tEXt()
    text.chunktEXt(png)

    # bKGD ********************************************************************************************
    print("-------------------------------------------------------------------------------------------")
    print("++++++++++++++++                  CHUNK bKGD                               ++++++++++++++++")
    print()
    bkgd = Chunk_bKGD.bKGD()
    if IHDR == -1:
        print("Chunk bKGD nie może być odczytany bo nie ma chunku IHDR")
    else:
        bkgd.chunkbKGD(png, IHDR.colorType)

    print("-------------------------------------------------------------------------------------------")
    print("++++++++++++++++                  CHUNK IDAT                               ++++++++++++++++")
    print()
    idat = Chunk_IDAT.IDAT()
    #idat.chunkIDAT(png)

    print(png[0:10])
else:
    print("Wczytany plik nie jest formatu PNG")