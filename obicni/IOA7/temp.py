# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
import matplotlib.pyplot as plt
import random as random

BROJAC = 100

def p(dE, Tk):
    return math.exp(-dE/Tk)

iter = 1
plt.figure()
x = [w for w in range(0, 100 * BROJAC)]
srednjeNajbolje = [0 for o in range(0, 100 * BROJAC)]

while iter <= 20:
    Tk = 50
    c = []
    suma = 0
    i = 0
    vrednosti = [random.randint(0, 1) for l in range(0, 100)]

    minT = 0
    for v in vrednosti:
        minT += v
    min = minT
    while i < 100:
        Tk *= 0.95
        brojac = 0
        while brojac < BROJAC:
            suma = 0
            promenjeno = [False for k in range(0, 100)]
            j = 100 - i
            while j > 0:
                indeks = random.randint(0, 99)
                while promenjeno[indeks]:
                    indeks = (indeks + 1) % len(vrednosti)
                promenjeno[indeks] = True
                vrednosti[indeks] = 1 - vrednosti[indeks]
                j -= 1
            
            for q in vrednosti:
                suma += q
            if suma < minT:
                minT = suma
                if suma < min:
                    min = suma
            elif random.random() < p(suma - minT, Tk):
                minT = suma
            else:
                r = 0
                while r < 100:
                    if promenjeno[r]:
                        vrednosti[r] = 1 - vrednosti[r]
                    r += 1
            c.append(min)
            srednjeNajbolje[i * BROJAC + brojac] += min
            brojac += 1
        i += 1

    plt.plot(x, c)
    plt.xlabel('iter')
    plt.ylabel('minT')
    iter += 1

m = 0
while m < BROJAC * 100:
    srednjeNajbolje[m] /= 20
    m += 1

plt.show()
plt.figure()
plt.plot(x, srednjeNajbolje)
plt.xlabel('iter')
plt.ylabel('srednje')
plt.show()