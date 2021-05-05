import Chunk_IEND
import Chunk_IHDR


def AnonimizePNG(filename, new_filename):
    # png magic number lets to know other programs that it is png file
    iend = Chunk_IEND.IEND()
    PNG_MAGIC_NUMBER = b'\x89PNG\r\n\x1a\n'
    IHDR = Chunk_IHDR.getrawIHDRcopy(filename)
    IEND = iend.getrawIENDcopy(filename)
    file_handler = open(new_filename, "wb")
    file_handler.write(PNG_MAGIC_NUMBER)
    for byteIHDR in IHDR:
        file_handler.write(byteIHDR)
    for byteIHDR in IEND:
        file_handler.write(byteIHDR)
    file_handler.close()

    return -1
