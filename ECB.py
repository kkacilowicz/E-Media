import RSA
from keyGenerator import Key
import Chunk_IDAT
import read
import PNG_RSA
from PIL import Image
import io

filename = "Images/images3.png"
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





print(len(png))

ECBEncryption(png)

print(" Start ==============================")
PNG_RSA.PNG_start(png)
print(" End ==============================")
PNG_RSA.PNG_end(png)

