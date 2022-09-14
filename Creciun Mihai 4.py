import math
def comb():
    n = int(input('n = '))
    m = int(input('m = '))
    if (n > m):
        c = math.factorial(n) / (math.factorial(m) * (math.factorial(n - m)))
        return c
    else:
        return "Dati alte numere (n > m)"
print(comb())  