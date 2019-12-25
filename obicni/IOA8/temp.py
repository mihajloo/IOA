import matplotlib.pyplot as plt
import random as random

BrojIndividuaUPopulaciji = 100
VRV_UKRSTANJA= 0.8
VRV_MUTACIJE = 0.1
BrIndividuaZaUkrstanje = BrojIndividuaUPopulaciji / 5
BROJ_ITERACIJA = 2000
BROJ_POKRETANJA = 20

def f(vrednosti):
    suma = 0
    for v in vrednosti:
        suma += v
    return suma


srednjeNajbolje = [0 for o in range(0, BROJ_ITERACIJA)]

plt.figure()
brojac = 0
while brojac < BROJ_POKRETANJA:
    c = []
    
    populacija = []
    i = 0
    while i < BrojIndividuaUPopulaciji:
        vrednosti = [random.randint(0, 1) for l in range(0, 100)]
        populacija.append(vrednosti)
        i += 1
    
    globalniMin = -1
    iteracija = 0
    while True:
        #selekcija: decimacija i elitizam
        min1 = 101
        min2 = 101
        min1Indeks = -1
        min2Indeks = -1
        maximum = -1
        maxIndex = -1
        
        indeks = 0
        while indeks < BrojIndividuaUPopulaciji:
            zbir = f(populacija[indeks])
            if(zbir < min1):
                min2 = min1
                min2Indeks = min1Indeks
                min1 = zbir
                min1Indeks = indeks
            elif (zbir < min2):
                min2 = zbir
                min2Indeks = indeks
            elif (zbir > maximum):
                maximum = zbir
                maxIndex = indeks
            indeks += 1
                        #populacija = sorted(populacija, key = f)        
        minimum = min1  #ako se koristi sortiranje treba da stoji minimum = f(populacija[0])
        if (globalniMin == -1 or minimum < globalniMin):
            globalniMin = minimum
        c.append(globalniMin)
        srednjeNajbolje[iteracija] += globalniMin
        
        if iteracija == BROJ_ITERACIJA - 1:
            break
        
        #ukrstanje
        if (random.random() < VRV_UKRSTANJA):
            indeksDoKogSeUkrsta = random.random() * 100
            i = 0
            novaIndividua = []
            while i < indeksDoKogSeUkrsta:
                novaIndividua.append(populacija[min1Indeks][i])#ako se koristi sortiranje umesto nalazenja dva min i max
                i += 1                                         #umesto min1Indeks i min2Indeks treba da stoji 0 i 1 respektivno
            while i < 100:                                     #a umesto maxIndex BrojIndividuaUPopulaciji - 1
                novaIndividua.append(populacija[min2Indeks][i])
                i += 1
            populacija[maxIndex] = novaIndividua
        
        #mutiranje 
        for p in populacija:
            if (random.random() < VRV_MUTACIJE):
                indeksKojiSeMutira = int(random.random() * 100)
                p[indeksKojiSeMutira] = 1 - p[indeksKojiSeMutira]
        
        iteracija += 1
    
    
    x = [w for w in range(0, iteracija + 1)]
    plt.plot(x, c)
    
    brojac += 1
    
plt.xlabel('iter')
plt.ylabel('min')    
plt.show()

i = 0
while i <= iteracija:
    srednjeNajbolje[i] /= BROJ_POKRETANJA
    i += 1

plt.figure()
plt.plot(x, srednjeNajbolje)
plt.xlabel('iter')
plt.ylabel('min')    
plt.show()