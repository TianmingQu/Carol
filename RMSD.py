#!/usr/bin/python3
# https://github.com/TianmingQu/Carol.git
import numpy as np
from math import sqrt
def readfile(filename):
    f = open(filename,'r')
    lines = f.readlines()
    x = []
    y = []
    z = []
    for line in lines:
        words = line.split()
        x.append(float(words[6]))
        y.append(float(words[7]))
        z.append(float(words[8]))
    return x,y,z

x = readfile('2FA9noend.pdb')
y = readfile('2FA9noend2mov.pdb')

def RMSD(x,y):
    R = []
    Xi = np.array(x[0])
    Yi = np.array(x[1])
    Zi = np.array(x[2])
    Xe = np.array(y[0])
    Ye = np.array(y[1])
    Ze = np.array(y[2])
    X = (Xi - Xe) ** 2
    Y = (Yi - Ye) ** 2
    Z = (Zi - Ze) ** 2
    for I in range(1337):
        R.append(X[I] + Y[I] + Z [I])
    return print(sqrt(sum(R)/1337))



RMSD(x,y)




