def float_list():
    n = int(input("Numarul de elemente: "))
    lista = []
    for i in range(0, n):
        num = float(input("Numarul: "))
        lista.append(num)
    return lista
print(float_list())