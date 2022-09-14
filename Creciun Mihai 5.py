a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))
def adf(numa1, numa2, numi1, numi2):
    #suma
    numitor = numi1 * numi2
    numarator = numa1*numi2 + numa2*numi1
    r = ((numa1*numi2 + numa2*numi1) / (numi1*numi2))
    return r
print(adf(a, b, c, d))
def inmf(numa1, numa2, numi1, numi2):
    #produs
    numitor = numi1 * numi2
    numarator = numa1 * numa2
    r = ((numa1 * numa2) / (numi1 * numi2))
    return r
print(inmf(a, b, c, d))