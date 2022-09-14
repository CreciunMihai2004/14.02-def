def int_list():
    n = int(input("Numarul de elemente: "))
    lista = []
    for i in range(0, n):
        num = int(input("Numarul: "))
        lista.append(num)
    return lista
print(int_list())