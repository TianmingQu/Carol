#!/usr/bin/python3
import numpy as np
f = open("2FA9noend.pdb",'r')
lines = f.readlines()
x = []
y = []
z = []
m = []
I = []
records = []
massdict = {"C":12.01,"N":14.01,"O":16.0,"S":32.06}
choice = input("Do you want to center by Mass or geometry 'M' or 'G':")
if choice == 'M':
    #center by mass
    for line in lines:
        words = line.split()
        I.append(words)
        atomdic = {}
        atomdic['x'] = float(words[6]) #Coordinate x
        atomdic['y'] = float(words[7]) #Coordinate y
        atomdic['z'] = float(words[8]) #Coordinate z
        element = words[11].strip()
        atomdic['element'] = element
        atomdic['mass'] = massdict[element]
        x.append(atomdic['x'])
        y.append(atomdic['y'])
        z.append(atomdic['z'])
        m.append(atomdic['mass'])
        Cx = np.array(x)
        Cy = np.array(y)
        Cz = np.array(z)
        M = np.array(m)
        Mx = sum(Cx * M) / sum(M)
        My = sum(Cy * M) / sum(M)
        Mz = sum(Cz * M) / sum(M)
        Cx = Cx[:] - Mx
        Cy = Cy[:] - My
        Cz = Cx[:] - Mz
else:
    for line in lines:
        words = line.split()
        I.append(words)
        atomdic = {}
        atomdic['x'] = float(words[6]) #Coordinate x
        atomdic['y'] = float(words[7]) #Coordinate y
        atomdic['z'] = float(words[8]) #Coordinate z
        element = words[11].strip()
        atomdic['element'] = element
        x.append(atomdic['x'])
        y.append(atomdic['y'])
        z.append(atomdic['z'])
        Cx = np.array(x)
        Cy = np.array(y)
        Cz = np.array(z)
        Gx = sum(Cx) / 1337
        Gy = sum(Cy) / 1337
        Gz = sum(Cz) / 1337
        Cx = Cx[:] - Gx
        Cy = Cy[:] - Gy
        Cz = Cx[:] - Gz
for i in range(1337):
    Atomdic = {}
    I[i][6] = Cx[i]
    I[i][7] = Cy[i]
    I[i][8] = Cz[i]
    Atomdic['num'] = I[i][1] #numebr of lines
    Atomdic['at'] = I[i][2]  #atom type
    Atomdic['aa'] = I[i][3] #amino acid
    Atomdic['C'] = I[i][4] #Chain ID
    Atomdic['RN'] = I[i][5] #residue number
    Atomdic['x'] = float(I[i][6]) #Coordinate x
    Atomdic['y'] = float(I[i][7]) #Coordinate y
    Atomdic['z'] = float(I[i][8]) #Coordinate z
    Atomdic['O'] = float(I[i][9]) #occupancy
    Atomdic['T'] = float(I[i][10]) #Temp factor
    Atomdic['element'] = I[i][11] #element type
    records.append(Atomdic)
f.close()
f = open("New_2FA9noend.pdb",'w')
for record in records:
    f.write("Atom      %4s  %-3s  %s %s  %3s      %7.3f  %7.3f  %7.3f  %3.2f %5.2f           %s" % (record['num'], record['at'], record['aa'], record['C'], record['RN'], record['x'], record['y'], record['z'],record['O'], record['T'], record['element']))
    f.write('\n')
f.close()