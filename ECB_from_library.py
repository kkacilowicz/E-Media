import rsa
import Chunk_IDAT
import read
import PNG_RSA

(pubkey, privkey) = rsa.newkeys(1024)  # tworzenie kluczy

filename = "Images/images3.png"
png = read.readPNG(filename)


def Encrypt(png, pubkey):
    idat = Chunk_IDAT.IDAT()
    IDAT_list = idat.getdateIDAT(png)  # lista IDAT ( same dane)
    filename = "RSA_library.png"
    PNG_RSA.PNG_start(png, filename)

    for i in range(0, len(IDAT_list)):
        crypto = rsa.encrypt(IDAT_list[i], pubkey)
        print(crypto)



Encrypt(png, pubkey)
