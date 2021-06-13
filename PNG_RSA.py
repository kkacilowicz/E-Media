import Chunk_IDAT
import read
from PIL import Image

def PNG_start(png):
    idat = Chunk_IDAT.IDAT()
    start_position = idat.getstartIDAT(png)
    tmp = png[0:start_position]
    print("start_position : ", start_position)
    print(len(png[0:start_position]))
    # PNG_MAGIC_NUMBER = b'\x89PNG\r\n\x1a\n'

    file = open("images_RSA.png", "wb")
    # file.write(PNG_MAGIC_NUMBER)
    k = 0
    for i in tmp:
        k = k + 1
        file.write(i)
    print("k ", k)

    file.close()

    # png_1=read.readPNG("images_RSA.png")
    # print(png_1)
    # print(len(png_1))


def PNG_end(png):
    idat = Chunk_IDAT.IDAT()
    end_position = idat.getendIDAT(png)
    tmp = png[end_position:]

    print("len : ", len(png))
    print(" end_ pos ", end_position)
    print(" len - end:", len(png) - end_position)


    file = open("images_RSA.png", "ab")
    # file.write(PNG_MAGIC_NUMBER)
    for i in tmp:
        file.write(i)

    file.close()

    # png_1=read.readPNG("images_RSA.png")
    # print(873+246)
    # print(png_1)
    # print(len(png_1))