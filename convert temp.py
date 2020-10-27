#!/usr/bin/python3
import sys
print('Please input a temperature:')
F = sys.stdin.readline()
F = float(F)
K = 5 / 9 * (F - 32) + 273
sys.stdout.write(str(K) + '\n')
