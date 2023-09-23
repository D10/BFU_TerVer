import math


class TerVer:

    def __init__(self, n: int | float, m: int | float, p: int | float, q: int | float):
        self.m = m
        self.n = n
        self.p = p
        self.q = q

    @classmethod
    def factorial(cls, x: int) -> int:

        if x == 0:
            return x

        x = abs(x)
        factorio = 1

        for i in range(1, x + 1):
            factorio *= i

        if x % 2 > 0:
            return factorio * -1

        else:
            return factorio

    def c(self) -> float:
        if not all([self.n, self.m]):
            print('division by zero in C')
            return 0

        return self.factorial(self.n) / (self.factorial(self.m) * self.factorial(self.n - self.m))

    def get_param(self) -> float:
        return abs((self.m - self.n * self.p) / (math.sqrt(self.n * self.p * self.q)))

    def gauss(self) -> float:
        return (1 / math.sqrt(2 * math.pi)) * (math.e ** -(self.get_param() / 2))

    def bernulli(self) -> float:
        return abs(self.c() * (self.p ** self.m) * self.q ** (self.n - self.m))

    def puasson(self) -> float | str:
        lam = self.n * self.p

        if lam > 10:
            return 'Непременимо в данном случае, т.к λ больше 10'

        return abs(((lam ** self.m) * (math.e ** -lam)) / self.factorial(m))

    def muavr_laplas(self) -> float | str:
        if self.n * self.p * self.q < 20:
            return 'Непременимо в данном случае, т.к npq меньше 20'

        return self.gauss() / (math.sqrt(self.n * self.p * self.q))

