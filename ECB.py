import RSA
from keyGenerator import Key
import Chunk_IDAT
import read
import PNG_RSA

filename = "Images/images3.png"
png = read.readPNG(filename)


def ECBEncryption(png):
    key = Key()
    key.generate_Keys()
    idat = Chunk_IDAT.IDAT()
    IDAT_list = idat.getdateIDAT(png)  # lista IDAT ( same dane)
    filename = "images_RSA.png"
    PNG_RSA.PNG_start(png, filename)

    # IDAT_list[0]-> to pierwszy chunk IDAT
    # IDAT_list[0][0] -> to pierwszy element danych w pierwszym chunku IDAT

    for i in range(0, len(IDAT_list)):

        blox_m = []

        if len(IDAT_list[i]) % 256 != 0:  # dopisanie zer tak aby wszędzie były pełne bloki
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

        encryption = []
        for m in blox_m:
            encryption_ = RSA.encryption(int.from_bytes(m, byteorder='big', signed=True), key.n, key.e)
            encryption.append(encryption_.to_bytes(encryption_.bit_length() + 7 // 8, byteorder='big'))

        sum = 0
        for s in range(0, len(encryption)):
            sum += len(encryption[s])

        size = sum.to_bytes(4, byteorder='big')

        PNG_RSA.PNG_new_IDAT(png, filename, size, encryption)

    PNG_RSA.PNG_end(png, filename)
    PNG_RSA.display_PNG(filename)


ECBEncryption(png)


