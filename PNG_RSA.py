import Chunk_IDAT
import read
from PIL import Image, ImageFile


def PNG_start(png, filename):
    idat = Chunk_IDAT.IDAT()
    [start_position, length] = idat.getstartIDAT(png)
    tmp = png[0:start_position]
    # print("start_position : ", start_position)
    # print(len(png[0:start_position]))
    # PNG_MAGIC_NUMBER = b'\x89PNG\r\n\x1a\n'

    file = open(filename, "wb")
    # file.write(PNG_MAGIC_NUMBER)
    k = 0
    for i in tmp:
        k = k + 1
        file.write(i)
    # print("k ", k)

    file.close()

    # png_1 = read.readPNG("images_RSA.png")
    # # print(png_1)
    # print("etap 1: ", len(png_1))


def PNG_new_IDAT(png, filename, length, data):
    idat = Chunk_IDAT.IDAT()

    [start_position, lengthData] = idat.getstartIDAT(png)
    end_position = start_position + lengthData + 4

    tmp = png[end_position - 4:end_position]

    file = open(filename, "ab")
    file.write(length)
    file.write(b'I')
    file.write(b'D')
    file.write(b'A')
    file.write(b'T')

    file.write(data)

    # for i in data:
    #     file.write(i)

    for i in tmp:
        file.write(i)

    file.close()

    # png_1 = read.readPNG("images_RSA.png")
    # f = open("tmp.txt", "w+")
    # for i in png_1:
    #     f.write(str(i) + " ")
    # f.close()
    # print("etap 2 len png 1: ", len(png_1))


def PNG_end(png, filename):
    idat = Chunk_IDAT.IDAT()
    end_position = idat.getendIDAT(png)
    tmp = png[end_position:]

    # print("len : ", len(png))
    # print(" end_ pos ", end_position)
    # print(" len - end:", len(png) - end_position)

    file = open(filename, "ab")
    # file.write(PNG_MAGIC_NUMBER)
    for i in tmp:
        file.write(i)

    file.close()

    png_1 = read.readPNG("images_RSA.png")
    # print(873+246)
    # print(png_1)
    # print("długość nowego:", len(png_1))


def display_PNG(filename):
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    image = Image.open(filename)
    bmpinfo = image.size
    print(bmpinfo)
    image.show()
