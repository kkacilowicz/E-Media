import Chunk_IDAT
import Chunk_IEND
import Chunk_IHDR


def AnonimizePNG(filename, new_filename):
    # png magic number lets to know other programs that it is png file
    iend = Chunk_IEND.IEND()
    idat = Chunk_IDAT.IDAT()
    PNG_MAGIC_NUMBER = b'\x89PNG\r\n\x1a\n'
    IHDR = Chunk_IHDR.getrawIHDRcopy(filename)
    IEND = iend.getrawIENDcopy(filename)
    IDAT = idat.getrawIDATscopy(filename)
    file_handler = open(new_filename, "wb")
    file_handler.write(PNG_MAGIC_NUMBER)
    for byteIHDR in IHDR:
        file_handler.write(byteIHDR)
    for byteIDAT in IDAT:
        file_handler.write(byteIDAT)
    for byteIEND in IEND:
        file_handler.write(byteIEND)
    file_handler.close()

    return -1
