# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 23:36:08 2019

@author: Tijana
"""

from scipy.optimize import minimize
import numpy as np
import random as random

N = 2
K = 1
c = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
#c = [0.1, 0.2, 0.4, 0.2, 0.09, 0.21, 0.3, 0.1, 0.12]
M = 9
Ax = [ -3, -3, -3, 0, 0, 0, 3, 3, 3 ]
Ay = [ -3, 0, 3, -3, 0, 3, -3, 0, 3 ]
iteracija=200
k=50
okolina=0.1
pomocni = [10, 10]
minimumi = []
minimumi.append(pomocni)

def f(x):
	suma = 0
	for i in range(M):
		suma += 1 / ((x[0] - Ax[i]) * (x[0] - Ax[i]) + (x[1] - Ay[i]) * (x[1] - Ay[i]) + c[i])
	return K-suma

def razdaljina(x,y):
    return ((x[0] - y[0])**2 + (x[1] - y[1])**2)**(1/2)

def faktorijel(n):
	fact= 1;
	for i in range(1,n+1):
		fact *= i
	return fact

def Q(n, k):
    suma = 0
    if (n == 1):
        return 1
    else:
        suma += n**k
        for p in range(1, n):
            suma -= ((faktorijel(n))/(faktorijel(p) * faktorijel(n-p)) )* Q(p,k)
        return suma

def P(n, k):
	return Q(n, k) /(n** k)

def main():
    rezultat = 0
    for i in range(iteracija):
        pronadjeno = 0
        minimumi = []
        minimumi.append(pomocni)
        for j in range(k):
            flag = 0
            x = np.array([random.randint(-4, 4),random.randint(-4, 4)])
            res = minimize(f, x, method='Nelder-Mead')
            for p in range(len(minimumi)):
                if (razdaljina(res.x, minimumi[p]) < okolina):
                    flag = 1
            if (flag == 0):
                pronadjeno+=1
                minimumi.append(res.x)
        if (pronadjeno == M): 
            rezultat+=1
    print(rezultat/iteracija)
    print(P(M,k))
    
if '_main_' == main():
    main()