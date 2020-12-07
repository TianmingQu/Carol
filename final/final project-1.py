#!/usr/bin/python3
# https://github.com/TianmingQu/Carol.git
# The pdb file should only contain atom information
import numpy as np
from matplotlib import pyplot as plt
from math import sqrt


# function to read in all the data for further calculation, user can enter the atom number they want and output the corresponding coordinates
def readfile_calD(filename):
    f = open(filename, 'r')  # read in file
    lines = f.readlines()
    atom1 = input('please enter the first atom number:')
    atom2 = input('please enter the second atom number:')
    atom1 = str(atom1)  # The atom I focus on this project is atom number 476 and 1280, but it can be user specific
    atom2 = str(atom2)
    # coordinates for the first atom
    x1 = []
    y1 = []
    z1 = []
    # coordinates for the second atom
    x2 = []
    y2 = []
    z2 = []
    for line in lines:
        words = line.split()
        if words[1] == atom1:
            x1.append(float(words[6]))
            y1.append(float(words[7]))
            z1.append(float(words[8]))
        if words[1] == atom2:
            x2.append(float(words[6]))
            y2.append(float(words[7]))
            z2.append(float(words[8]))
    # Turn all coordinates into numpy array
    X1 = np.array(x1)
    Y1 = np.array(y1)
    Z1 = np.array(z1)
    X2 = np.array(x2)
    Y2 = np.array(y2)
    Z2 = np.array(z2)
    # there are total 5354 frames in the reading file, so 5666 distances can be calculated. For different pdn files, the number of frames can be manually changed.
    D = []
    T = []
    for i in range(5666):
        d = sqrt((X1[i] - X2[i]) ** 2 + (Y1[i] - Y2[i]) ** 2 + (Z1[i] - Z2[i]) ** 2)
        D.append(d)
        # time step for saving each frame is 40ps
        t = i / 25
        T.append(t)
    x = np.array(T)
    y = np.array(D)
    plt.plot(x, y)
    plt.xlabel('T')
    plt.ylabel('D')
    plt.show()


def readfile_calDihedral(filename):
    f = open(filename, 'r')  # read in file
    lines = f.readlines()
    atom1 = input('please enter the first atom number:') # The atom number for result plot is: D400(1234-1233-1238-1240) and F401(1234-1233-1246-1248)
    atom2 = input('please enter the second atom number:')
    atom3 = input('please enter the third atom number:')
    atom4 = input('please enter the fourth atom number:')
    # coordinates for the first atom
    x1 = []
    y1 = []
    z1 = []
    # coordinates for the second atom
    x2 = []
    y2 = []
    z2 = []
    # coordinates for the third atom
    x3 = []
    y3 = []
    z3 = []
    # coordinates for the fourth atom
    x4 = []
    y4 = []
    z4 = []
    for line in lines:
        words = line.split()
        if words[1] == atom1:
            x1.append(float(words[6]))
            y1.append(float(words[7]))
            z1.append(float(words[8]))
        if words[1] == atom2:
            x2.append(float(words[6]))
            y2.append(float(words[7]))
            z2.append(float(words[8]))
        if words[1] == atom3:
            x3.append(float(words[6]))
            y3.append(float(words[7]))
            z3.append(float(words[8]))
        if words[1] == atom4:
            x4.append(float(words[6]))
            y4.append(float(words[7]))
            z4.append(float(words[8]))
    # Turn all coordinates into numpy array
    X1 = np.array(x1)
    Y1 = np.array(y1)
    Z1 = np.array(z1)
    X2 = np.array(x2)
    Y2 = np.array(y2)
    Z2 = np.array(z2)
    X3 = np.array(x3)
    Y3 = np.array(y3)
    Z3 = np.array(z3)
    X4 = np.array(x4)
    Y4 = np.array(y4)
    Z4 = np.array(z4)
    angel = []
    T = []
    A1 = []
    A2 = []
    A3 = []
    A4 = []
    for i in range(5666):
        A = (X2[i] - X1[i], Y2[i] - Y1[i], Z2[i] - Z1[i])  # define four vectors
        B = (X2[i] - X3[i], Y2[i] - Y3[i], Z2[i] - Z3[i])
        C = (X3[i] - X2[i], Y3[i] - Y2[i], Z3[i] - Z2[i])
        d = (X2[i] - X4[i], Y2[i] - Y4[i], Z2[i] - Z4[i])
        A1.append(A)
        A2.append(B)
        A3.append(C)
        A4.append(d)
        t = i / 25
        T.append(t)
    N1 = np.cross(A1, A2)  # two normal factors of two plates
    N2 = np.cross(A3, A4)
    # calculation of dihedral angel
    for i in range(5666):
        cos = np.dot(N1[i], N2[i].T) / np.linalg.norm(N1[i] * np.linalg.norm(N2[i]))
        r = np.arccos(cos)
        D = np.degrees(r)
        angel.append(D)

    x = np.array(T)
    y = np.array(angel)
    plt.plot(x, y)
    plt.xlabel('T')
    plt.ylabel('Angel')
    plt.show()


def openHTML(f, title):
    f.write("""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
""")
    f.write("<head>\n")
    f.write("<title>%s</title>\n" % title)
    f.write("</head>\n")
    f.write("<body>\n")


def writeHTMLImage(f, title, imgpath):
    f.write('<p class="">%s</p>\n' % title)
    f.write('<img src="%s" />\n' % imgpath)


def closeHTML(f):
    f.write("</body>\n")
    f.write("</html>\n")
    f.close()


if __name__ == "__main__":
    File1 = str(input('please enter pdb filename :'))  # for distance cal and Dihedral angel cal
    readfile_calD(File1)
    readfile_calDihedral(File1)
    f = open('final.html', 'w')
    openHTML(f, "final project")
    f.write("<h1>Analysis of Abl kinase conformation</h1>\n")
    writeHTMLImage(f, "Distance change of specific atom：The distance between two residues shows a dramatic decrease after about 50ns, which indicates a conformational change of aC-helix, also the distance stays around 7Å for the rest of time, which shows a lifetime for the new conformation", 'Distance.png')
    writeHTMLImage(f, "Dihedral Angel change of D400: The dihedral angel of D400 increases and keep fluctuating around 70 degree, with time increasing, which indicates a processing of DFG flip, the angel will further increase", 'D400.png')
    writeHTMLImage(f, "Dihedral Angel change of F401: The dihedral angel of F401 shows no obvious change, which is consistent with the trajectory that for current stage there is no obvious conformational change for F401 residue", 'F401.png')
    closeHTML(f)
    f.close()
