import RSA
from keyGenerator import Key
import Chunk_IDAT
import read
import PNG_RSA
import random

filename = "Images/images3.png"
png = read.readPNG(filename)
print("długośc png orygianlnego: ", len(png))

class CBC:
    def __init__(self):
        self.keysize_ = 1024
        self.keysize = self.keysize_ // 8
        self.size_block = self.keysize_ // 8 - 1
        self.IV = random.getrandbits(self.size_block)

    # m - blok. v - wektor

    def xor(self, m, v):
        return m ^ v

    def CBCEncryption(self, png, n, e):
        idat = Chunk_IDAT.IDAT()
        IDAT_list = idat.getdateIDAT(png)  # lista IDAT ( same dane)

        filename = "images_CBC_encryption.png"
        PNG_RSA.PNG_start(png, filename)
        block_size = self.size_block

        IV = self.IV
        encryption = []

        for i in range(0, len(IDAT_list)):

            block_m = []
            tmp = []
            k = -1

            for j in range(0, len(IDAT_list[i])):

                if len(tmp) == 0:
                    tmp.append(IDAT_list[i][j])
                else:
                    foo = b''.join([tmp[0], IDAT_list[i][j]])
                    tmp.insert(0, foo)

                if (j + 1) % block_size == 0 and j != 0:
                    k += 1
                    block_m.append(tmp[0])
                    xor_ = self.xor(int.from_bytes(block_m[k], byteorder='big'), IV)
                    encryption_ = RSA.encryption(xor_, n, e)  # wynik RSA - liczba
                    r = encryption_.to_bytes(self.keysize, byteorder='big')
                    IV = int.from_bytes(r, byteorder='big')
                    encryption.append(r)  # wyniki RSA jako tablice bajtów
                    tmp = []

            tmp2 = []  # dodane że wszystkie bloki łączą się w całość
            for e in range(0, len(encryption)):
                if len(tmp2) == 0:
                    tmp2.append(encryption[0])
                else:
                    foo = b''.join([tmp2[0], encryption[e]])
                    tmp2.insert(0, foo)

            size = len(tmp2[0]).to_bytes(4, byteorder='big')
            PNG_RSA.PNG_new_IDAT(png, filename, size, tmp2[0])

        PNG_RSA.PNG_end(png, filename)
        PNG_RSA.display_PNG(filename)


    def CBCDecrytpion(self, filenameEncryption, n, d):
        idat = Chunk_IDAT.IDAT()
        png = read.readPNG(filenameEncryption)
        # print(png)
        IDAT_list = idat.getdateIDAT(png)  # lista IDAT ( same dane)
        filename = "images_CBC_decryption.png"
        PNG_RSA.PNG_start(png, filename)

        IV = self.IV
        decryption = []

        for i in range(0, len(IDAT_list)):

            block_c = []
            tmp = []
            k = -1

            for j in range(0, len(IDAT_list[i])):

                if len(tmp) == 0:
                    tmp.append(IDAT_list[i][j])
                else:
                    foo = b''.join([tmp[0], IDAT_list[i][j]])
                    tmp.insert(0, foo)

                if (j + 1) % self.keysize == 0 and j != 0:
                    k += 1
                    block_c.append(tmp[0])
                    decryption_ = RSA.decryption(int.from_bytes(block_c[k], byteorder='big', signed=True), n, d)  # wynik RSA - liczba
                    xor_ = self.xor(IV, decryption_)
                    IV = xor_
                    decryption.append(xor_.to_bytes(self.size_block, byteorder='big'))  # wyniki RSA jako tablice bajtów
                    tmp = []

            tmp2 = []  # dodane że wszystkie bloki łączą się w całość
            for e in range(0, len(decryption)):
                if len(tmp2) == 0:
                    tmp2.append(decryption[0])
                else:
                    foo = b''.join([tmp2[0], decryption[e]])
                    tmp2.insert(0, foo)

            size = len(tmp2[0]).to_bytes(4, byteorder='big')
            PNG_RSA.PNG_new_IDAT(png, filename, size, tmp2[0])

        PNG_RSA.PNG_end(png, filename)
        PNG_RSA.display_PNG(filename)


key = Key()
key.generate_Keys()
cbc = CBC()
cbc.CBCEncryption(png, key.n, key.e)
cbc.CBCDecrytpion("images_CBC_encryption.png", key.n, key.d)
