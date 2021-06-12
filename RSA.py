# Algorytm RSA
# m - blok
# n  = p * q, gdzie p i q to liczby pierwsze losowe
# e - klucz publiczny
# d - klucz prywatny

def encryption(m, n, e):
    return pow(m, e, n)


def decryption(c, n, d):
    return pow(c, d, n)