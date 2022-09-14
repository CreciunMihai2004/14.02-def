def suma():
    s = 1 + sum([0.5**j for j in range(2, 9, 2)])
    return s
print(suma())