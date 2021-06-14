import random
import secrets


class Key:
    def __init__(self):
        self.p = 0
        self.q = 0
        self.n = 0
        self.e = 0
        self.d = 0
        self.p_q = 0
        self.keysize = 1024

    def test_Miller_Rabin(self, n, k):
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
        for i in range(k):  # k to liczba różnych testowanych wartości  a
            a = random.randrange(2, n - 1)  # wybór losowej liczby a z zbioru {2, ..., n -1 }
            x = pow(a, s, n)  # a ^ s mod n
            if x == 1 or x == n - 1:
                continue
            for j in range(r - 1):
                x = pow(x, 2, n)  # x^2 mod n
                if x == n - 1:
                    break
            else:
                return False
        return True

    def generate_p(self):
        p = 0

        while not self.test_Miller_Rabin(p, 200):  # dopóki nie znajdzie się w 200 iteracjach
            p = secrets.randbelow(2 ** (self.keysize // 2))

        self.p = p

    def generate_q(self):
        q = 0

        while not self.test_Miller_Rabin(q, 200):  # dopóki nie znajdzie się w 200 iteracjach
            q = secrets.randbelow(2 ** (self.keysize // 2))

        self.q = q

    def GCD(self, a, b):  # GCD - gratest common divisor - największy wspólny dzielnik
                          # sprawdzenie czy liczba względnie pierwsza
        if b != 0:        # liczba względnie pierwsza jak największy wspólny dzielnik to 1
            return self.GCD(b, a % b)
        else:
            return a

    def generate_e(self):
        n = self.p * self.q
        self.n = n
        size_n = n.bit_length()

        self.p_q = (self.p - 1) * (self.q - 1)

        while True:
            e = secrets.randbelow(2 ** size_n)
            if self.GCD(e, self.p_q) == 1 and e < self.n:
                break
        self.e = e

    def generate_d(self):
        d = pow(self.e, -1, self.p_q)
        assert self.GCD(d, self.n) == 1, " incorrect value of d "
        self.d = d

    def generate_Keys(self):
        self.generate_p()
        self.generate_q()
        self.generate_e()
        self.generate_d()

        publicKey = (self.e, self.n)
        privateKey = (self.d, self.n)

        return publicKey, privateKey
