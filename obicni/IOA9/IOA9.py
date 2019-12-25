import math
import random as random

Nint = 5
mmax = 10
D = 2 * Nint


def fk(x, m):
    return math.pow(x, m) * math.log(x)


def f(x, w):
    sumaM = 0
    m = 1
    while m <= mmax:
        sumaK = 0
        k = 0
        while k < Nint:
            sumaK += w[k] * fk(x[k], m)
            k += 1
        sumaM += abs(sumaK + 1 / math.pow(m + 1, 2)) / (1 / math.pow(m + 1, 2))
        m += 1
    return sumaM / mmax


F = 0.8
CR = 0.9
brUPopulaciji = 10 * D

prvi = 1
najboljeResenje = []
najboljaV = -1

populacija = []

i = 0
while i < brUPopulaciji:
    resenje = [random.random() for l in range(0, D)]
    treV = f(resenje[0:int(D / 2)], resenje[int(D / 2):D])
    if abs(treV) < abs(najboljaV) or prvi == 1:
        najboljeResenje = resenje
        najboljaV = treV
        prvi = 0
    populacija.append(resenje)
    i += 1

iteracije = 0
while iteracije < 1000:
    p = 0
    while p < brUPopulaciji:
        #selekcija
        x = populacija[p]
        aind = random.randint(0, D)
        while (aind == p):
            aind = (aind + 1) % D
        bind = random.randint(0, D)
        while (bind == p or bind == aind):
            bind = (bind + 1) % D
        cind = random.randint(0, D)
        while (cind == p or cind == aind or cind == bind):
            cind = (cind + 1) % D
        a = populacija[aind]
        b = populacija[bind]
        c = populacija[cind]

        #ukrstanje
        z = []
        j = 0
        while j < D:
            z.append(a[j] + F*(b[j] - c[j]))
            j += 1
        y = [0 for rte in range(0, D)]
        R = random.randint(1, D)
        i = 1
        while i <= D:
            ri = random.random()
            if ri < CR or R == i:
                y[i - 1] = z[i - 1]
            else:
                y[i - 1] = x[i - 1]
            if y[i - 1] < 0:
                y[i - 1] = 0.00000001
            if y[i - 1] > 1:
                y[i - 1] = 0.99999999
            i += 1

        xV = f(x[0:int(D / 2)], x[int(D / 2):D])
        yV = f(y[0:int(D / 2)], y[int(D / 2):D])
        if abs(yV) < abs(xV):
            populacija[p] = y
        if abs(yV) < abs(najboljaV):
            najboljeResenje = y
            najboljaV = yV
        p += 1
    iteracije += 1


print(najboljaV)
print(najboljeResenje)

def analitickoResenje(m):
    return -1.0/math.pow(m + 1, 2)

def mojeResenje(x, w, m):
    suma = 0
    k = 0
    while k < Nint:
        suma += w[k] * fk(x[k], m)
        k += 1
    return suma

m = 1
while m <= mmax:
    print(analitickoResenje(m), ' ', mojeResenje(najboljeResenje[0 : Nint], najboljeResenje[Nint : D], m))
    m += 1