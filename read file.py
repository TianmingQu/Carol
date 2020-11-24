#!/usr/bin/python3
# https://github.com/TianmingQu/Carol.git
f = open("2FA9noend.pdb",'r')  # read in file
lines = f.readlines()
records = []
I = []
for line in lines:
    words = line.split()
    I.append(words)
for i in range(1337):
    Atomdic = {}
    Atomdic['num'] = I[i][1]  # numebr of lines
    Atomdic['at'] = I[i][2]  # atom type
    Atomdic['aa'] = I[i][3]  # amino acid
    Atomdic['C'] = I[i][4]  # Chain ID
    Atomdic['RN'] = I[i][5]  # residue number
    Atomdic['x'] = float(I[i][6])  # Coordinate x
    Atomdic['y'] = float(I[i][7])  # Coordinate y
    Atomdic['z'] = float(I[i][8])  # Coordinate z
    Atomdic['O'] = float(I[i][9])  # occupancy
    Atomdic['T'] = float(I[i][10])  # Temp factor
    Atomdic['element'] = I[i][11]  # element type
    records.append(Atomdic)
f.close()
f = open("New_2FA9noend.pdb",'w')
for record in records:
    f.write("Atom      %4s  %-3s  %s %s  %3s      %7.3f  %7.3f  %7.3f  %3.2f %5.2f           %s" % (record['num'], record['at'], record['aa'], record['C'], record['RN'], record['x'], record['y'], record['z'],record['O'], record['T'], record['element']))
    f.write('\n')
f.close()
