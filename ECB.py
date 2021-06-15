import RSA
from keyGenerator import Key
import Chunk_IDAT
import read
import PNG_RSA

filename = "Images/images3.png"
png = read.readPNG(filename)

# f = open("original.txt", "w+")
# for i in png:
#     f.write(str(i) + " ")
# f.close()

# print("len png oryg: ", len(png) )

class ECB:
    def __init__(self):
        self.keysize_ = 1024
        self.keysize = self.keysize_ // 8
        self.size_block = self.keysize_ // 8 - 1



    def ECBEncryption(self, png, n, e):
        idat = Chunk_IDAT.IDAT()
        IDAT_list= idat.getdateIDAT(png)  # lista IDAT ( same dane)
        # IDAT_list = IDAT_[0:2 * self.size_block]
        filename = "images_RSA.png"
        PNG_RSA.PNG_start(png, filename)

        # IDAT_list[0]-> to pierwszy chunk IDAT
        # IDAT_list[0][0] -> to pierwszy element danych w pierwszym chunku IDAT

        encryption = []
        for i in range(0, len(IDAT_list)):
            self.original_length = len(IDAT_list[i])
            blox_m = []
            #
            # if len(IDAT_list[i]) % 120 != 0:  # dopisanie zer tak aby wszędzie były pełne bloki
            #     mod = len(IDAT_list[i]) % 120
            #     add = 120 - mod
            #     for k in range(0, add):
            #         IDAT_list[i].append(b'\x00')
            tmp = []

            for j in range(0, len(IDAT_list[i])):
                if len(tmp) == 0:
                    tmp.append(IDAT_list[i][j])
                else:
                    foo = b''.join([tmp[0], IDAT_list[i][j]])
                    tmp.insert(0, foo)

                if (j + 1) % self.size_block == 0 and j != 0:
                    blox_m.append(tmp[0])
                    tmp = []


            for m in blox_m:
                encryption_ = RSA.encryption(int.from_bytes(m, byteorder='big'), n, e)
                encryption.append(encryption_.to_bytes(self.keysize, byteorder='big'))

            tmp2 = [] # dodane że wszystkie bloki łączą się w całość
            for e in range(0, len(encryption)):
                if len(tmp2) == 0:
                    tmp2.append(encryption[0])
                else:
                    foo = b''.join([tmp2[0], encryption[e]])
                    tmp2.insert(0, foo)

            size = len(tmp2[0]).to_bytes(4, byteorder='big')
            print("size: ", size)
            PNG_RSA.PNG_new_IDAT(png, filename, size, tmp2[0])

        PNG_RSA.PNG_end(png, filename)
        PNG_RSA.display_PNG(filename)

    def ECBDecryption(self, filenameEncryption, n, d):
        idat = Chunk_IDAT.IDAT()
        png = read.readPNG(filenameEncryption)
        IDAT_list = idat.getdateIDAT(png)  # lista IDAT ( same dane)
        filename = "Encryption.png"

        PNG_RSA.PNG_start(png, filename)

        for i in range(0, len(IDAT_list)):
            blox_c = []

            tmp = []
            for j in range(0, len(IDAT_list[i])):
                if len(tmp) == 0:
                    tmp.append(IDAT_list[i][j])
                else:
                    foo = b''.join([tmp[0], IDAT_list[i][j]])
                    tmp.insert(0, foo)

                if (j + 1) % self.keysize == 0 and j != 0:
                    blox_c.append(tmp[0])
                    tmp = []

            descryption = []
            for c in blox_c:
                descryption_ = RSA.decryption(int.from_bytes(c, byteorder='big', signed=True), n, d)
                descryption.append(descryption_.to_bytes(self.size_block, byteorder='big'))


            tmp2 = [] # dodane że wszystkie bloki łączą się w całość
            for e in range(0, len(descryption)):
                if len(tmp2) == 0:
                    tmp2.append(descryption[0])
                else:
                    foo = b''.join([tmp2[0], descryption[e]])
                    tmp2.insert(0, foo)

            size = len(tmp2[0]).to_bytes(4, byteorder='big')
            print(int.from_bytes(size, byteorder='big', signed=True))

            PNG_RSA.PNG_new_IDAT(png, filename, size, tmp2[0])

        PNG_RSA.PNG_end(png, filename)
        PNG_RSA.display_PNG(filename)

key = Key()
key.generate_Keys()
ECB = ECB()

ECB.ECBEncryption(png, key.n, key.e)
ECB.ECBDecryption("images_RSA.png", key.n, key.d)

