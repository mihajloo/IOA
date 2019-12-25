# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt 
import numpy as np

file= open('izlaz.txt','r')

e=[]
vbe=[]
ic=[]
vout=[]

for line in file:
    s= line.split()
    if(len(s)!=0):
        vbe.append(float(s[0]))
        ic.append(float(s[1]))
        vout.append(float(s[2]))
        e.append(float(s[3]))
        
        
plt.figure()
plt.plot(e,vbe)
plt.xlabel('E')
plt.ylabel('Vbe')

plt.figure()
plt.plot(e,ic)
plt.xlabel('E')
plt.ylabel('ic')

plt.figure()
plt.plot(e,vout)
plt.xlabel('E')
plt.ylabel('Vout')
        

