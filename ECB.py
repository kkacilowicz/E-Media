import RSA
from keyGenerator import Key
import Chunk_IDAT
import read
from PIL import Image
import io

filename = "Images/images2.png"
png = read.readPNG(filename)


def ECBEncryption(png):
    key = Key()
    key.generate_Keys()
    idat = Chunk_IDAT.IDAT()
    IDAT_list = idat.getdateIDAT(png) # lista IDAT ( same dane)

    idat.getstartIDAT(png)
    idat.getendIDAT(png)

    # IDAT_list[0]-> to pierwszy chunk IDAT
    # IDAT_list[0][0] -> to pierwszy element danych w pierwszym chunku IDAT
    # print(IDAT_list[0])
    # print(IDAT_list[0][256])

    for i in range(0, len(IDAT_list)):

        blox_m = []

        if len(IDAT_list[i]) % 256 != 0: # dopisanie zer tak aby wszędzie były pełne bloki
            mod = len(IDAT_list[0]) % 256
            add = 256 - mod
            for k in range(0, add):
                IDAT_list[0].append(b'\x00')

        tmp = []

        for j in range(0, len(IDAT_list[i])):
            if len(tmp) == 0:
                tmp.append(IDAT_list[i][j])
            else:
                foo = b''.join([tmp[0], IDAT_list[i][j]])
                tmp.insert(0, foo)

            if (j + 1) % 256 == 0 and j != 0:
                blox_m.append(tmp[0])
                tmp = []
                # TU SĄ POPRAWNIE ZROBIONE BLOKI PO 256 ELEMENTÓW , TRZEBA JE ZASZYFROWAĆ, ZAMIENIĆ NA BAJTY I DO PLIKU PNG



        print(blox_m)
        print(len(blox_m))






ECBEncryption(png)







#
# idat = Chunk_IDAT.IDAT()
# position = idat.search(png, 0, len(png),  b'I', b'D', b'A', b'T')
# a = idat.getdateIDAT(png)
# # print(len(a))
# print("position:", position)
# print(png[877:885])
# table_of_m = []
# k = 0
# tmp = []
# index = 0
#
# # 105 wychodzi z len(a) % 256
# print(len(a) + 256 - 105)
# dod = 256 - 105
#
#
# for i in a:
#     if index == 256:
#         table_of_m.append(tmp[0])
#         tmp = []
#         index = 0
#
#     if len(tmp) == 0:
#         tmp.append(a[0])
#         keyword = tmp[0]
#         index = index + 1
#     else:
#         keyword = b''.join([tmp[0], i])
#         tmp.insert(0, keyword)
#         index = index + 1
#
#
# # print(table_of_m)
# print(len(table_of_m))
#
# new_png = []
#
# for i in range(0, len(table_of_m)):
#     new_png.append(RSA.encryption(int.from_bytes(table_of_m[i], byteorder='big', signed=True), key.n, key.e))
#
# # print(new_png)
# image_table = []
# for i in range(0, len(new_png)):
#     image_table.append(new_png[0].to_bytes(new_png[i].bit_length() + 7 // 8, 'big'))
#
# # print(image_table)
#
# image_to_show = []
# for i in image_table:
#     if len(image_to_show) == 0:
#         image_to_show.append(image_table[0])
#         keyword = image_to_show[0]
#     else:
#         keyword = b''.join([image_to_show[0], i])
#         image_to_show.insert(0, keyword)
#
#
# # print(image_to_show)
#
# img = Image.open(io.BytesIO(image_to_show[0]))
# img.show()
#
#
#
# # img = Image.new( 'RGB', (100,100), "black") # Create a new black image
# # pixels = img.load() # Create the pixel map
# # for i in range(img.size[0]):    # For every pixel:
# #     for j in range(img.size[1]):
# #         pixels[i,j] = (i, j, image_tabel[i]) # Set the colour accordingly
# #
# # img.show()
# #
# # plik = open("obraz.png", "w+")
# # plik.write(str(b'\x89PNG\r\n\x1a\n'))
# # if plik.writable():
# #     plik.write(str(new_png))
# #
# # im = Image.open("obraz.png")
# # im.show()
#
# # w sumie 2 pytania do Grzesia : pierwsze czy jak robił bloki to czy łączył bity,
# # drugie : czy wynik szyfrowania to poprostu ciąg cyfr, czy trzeba zmienić je na bajty
# # jak się robi obraz , czy trzeba wszystkie chunki przepisac
