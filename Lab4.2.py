import math


def func(x0, x1, x2):
    S = 4.17 * math.sqrt(t) - math.sin(math.pi * x1 + (math.pi / 7)) + math.e ** ((x2 / x0) + x1)
    return (S)


t = float(input("Введіть t:"))
n = float(input("Введіть n:"))
k = float(input("Введіть k:"))
S = func(t,n,k)
print(S)
