import RSA
from keyGenerator import Key
import Chunk_IDAT
import read
import PNG_RSA
import secrets

filename = "Images/ball.png"
png = read.readPNG(filename)
print("długośc png orygianlnego: ", len(png))


# m - blok. v - wektor

def xor(m, v):
    return m ^ v


def CBCEncryption(png, n, e):
    idat = Chunk_IDAT.IDAT()
    IDAT_list = idat.getdateIDAT(png)  # lista IDAT ( same dane)
    filename = "images_RSA.png"
    PNG_RSA.PNG_start(png, filename)
    block_size = 256

    IV = secrets.randbelow(2 ** block_size)

    encryption = []

    for i in range(0, len(IDAT_list)):

        block_m = []
        tmp = []
        k = -1

        if len(IDAT_list[i]) % 256 != 0:  # dopisanie zer tak aby wszędzie były pełne bloki
            mod = len(IDAT_list[0]) % 256
            add = 256 - mod
            for l in range(0, add):
                IDAT_list[0].append(b'\x00')

        for j in range(0, len(IDAT_list[i])):

            if len(tmp) == 0:
                tmp.append(IDAT_list[i][j])
            else:
                foo = b''.join([tmp[0], IDAT_list[i][j]])
                tmp.insert(0, foo)

            if (j + 1) % block_size == 0 and j != 0:
                k += 1
                block_m.append(tmp[0])
                xor_ = xor(int.from_bytes(block_m[k], byteorder='big', signed=True), IV)
                encryption_ = RSA.encryption(xor_, n, e)  # wynik RSA - liczba
                r = encryption_.to_bytes(n.bit_length(), byteorder='big')
                IV = int.from_bytes(r, byteorder='big', signed=True)
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


def CBCDecrytpion(filenameEncryption, n, d):
    idat = Chunk_IDAT.IDAT()
    png = read.readPNG(filenameEncryption)
    # print(png)
    IDAT_list = idat.getdateIDAT(png)  # lista IDAT ( same dane)
    filename = "images_CBC_decryption.png"
    PNG_RSA.PNG_start(png, filename)
    block_size = n.bit_length()
    print("długość n:", n.bit_length())

    IV = secrets.randbelow(2 ** block_size)

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

            if (j + 1) % block_size == 0 and j != 0:
                k += 1
                block_c.append(tmp[0])
                decryption_ = RSA.decryption(int.from_bytes(block_c[k], byteorder='big', signed=True), n,
                                             d)  # wynik RSA - liczba
                xor_ = xor(IV, decryption_)
                IV = xor_
                decryption.append(xor_.to_bytes(n.bit_length(),
                                                byteorder='big'))  # wyniki RSA jako tablice bajtów
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
CBCEncryption(png, key.n, key.e)
CBCDecrytpion("images_RSA.png", key.n, key.d)
