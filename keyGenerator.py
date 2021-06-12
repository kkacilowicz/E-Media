import os
import random


def test_Miller_Rabin(n, k):
    # n - nieparzysta liczba naturalna do przetestowania
    # k - parametr określający dokładność testu

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n < 2:
        return False

    r = 0
    s = n - 1

    while s % 2 == 0:
        r = r + 1
        s = s // 2
    for i in range(k): # k to liczba różnych testowanych wartości  a
        a = random.randrange(2, n - 1) # wybór losowej liczby a z zbioru {2, ..., n -1 }
        x = pow(a, s, n) # a ^ s mod n
        if x == 1 or x == n - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, n) # x^2 mod n
            if x == n - 1:
                break
        else:
            return False
    return True


def generate_p():

    size = 100 # potem trzeba zmienić size na 550

    p = b'\x00' # na początku p to 0
    while not test_Miller_Rabin(int.from_bytes(p, byteorder='big', signed=True), 100): # dopóki nie znajdzie się w 100 iteracjach
        print("szukam p ")
        p = os.urandom(size)                                                           # że p liczba pierwsza to losuj nowe

    return p

def generate_q():

    size = 80 # później trzeba zmienić na 480
    q = b'\x00'  # na początku p to 0
    while not test_Miller_Rabin(int.from_bytes(q, byteorder='big', signed=True),
                                100):  # dopóki nie znajdzie się w 100 iteracjach
        q = os.urandom(size)  # że p liczba pierwsza to losuj nowe

    return q

def NWD(a,b): # sprawdzenie czy liczba względnie pierwsza
    if b != 0:  # liczba względnie pierwsza jak największy wspólny dzielnik to 1
        return NWD(b, a % b)
    else:
        return a

def generate_e():
    p = generate_p()
    p_ = int.from_bytes(generate_p(), byteorder='big', signed=True)
    print("mam p ", p)
    q = generate_q()
    q_ = int.from_bytes(generate_q(), byteorder='big', signed=True)
    print("mam q ", q)
    tmp = (p_ - 1)*(q_ - 1)
    n = p_ * q_
    print("dł p: ", p.bit_length())
    print("dł q: ", q.bit_length())
    print("dł n: ", n.bit_length())
    # print("szukam e")
    # while True:
    #     e = os.urandom(1024)
    #     print("losuje ....")
    #     e_int = int.from_bytes(e, byteorder='big', signed=True)
    #     if (NWD(e_int, tmp) == 1 and e_int < tmp):
    #         print("ta dam")
    #     if (NWD(e_int, tmp) == 1 and e_int < n):
    #         print("break")
    #         break;

    return e

e = generate_e()
print(e)