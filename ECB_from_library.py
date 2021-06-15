import rsa
import Chunk_IDAT
import read
import PNG_RSA

(pubkey, privkey) = rsa.newkeys(1024)  # tworzenie kluczy

filename = "Images/images3.png"
png = read.readPNG(filename)


class ECB_Library:
    def __init__(self):
        self.keysize_ = 1024
        self.keysize = self.keysize_ // 8
        self.size_block = 117

    def Encrypt(self, png, pubkey):
        idat = Chunk_IDAT.IDAT()
        IDAT_list = idat.getdateIDAT(png)  # lista IDAT ( same dane)
        filename = "RSA_library.png"
        PNG_RSA.PNG_start(png, filename)

        # IDAT_list[0]-> to pierwszy chunk IDAT
        # IDAT_list[0][0] -> to pierwszy element danych w pierwszym chunku IDAT

        encryption = []
        for i in range(0, len(IDAT_list)):

            blox_m = []
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
                encryption_ = rsa.encrypt(m, pubkey)
                encryption.append(encryption_)

            tmp2 = []  # dodane że wszystkie bloki łączą się w całość
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

    def Decryption(self, filename, privkey):
        idat = Chunk_IDAT.IDAT()
        png = read.readPNG(filename)
        IDAT_list = idat.getdateIDAT(png)  # lista IDAT ( same dane)
        filename = "RSA_library_decrytpion.png"

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
                descryption_ = rsa.decrypt(c, privkey)
                descryption.append(descryption_)


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


ECBlibrary = ECB_Library()
ECBlibrary.Encrypt(png, pubkey)
ECBlibrary.Decryption("RSA_library.png", privkey)
