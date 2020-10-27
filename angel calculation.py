#!/usr/bin/python3
import sys
import math
print('Please enter the coordinate for point A  B and C: ')
a1 = sys.stdin.readline()
a2 = sys.stdin.readline()
b1 = sys.stdin.readline()
b2 = sys.stdin.readline()
c1 = sys.stdin.readline()
c2 = sys.stdin.readline()
AB = math.hypot(float(a1) - float(b1), float(a2) - float(b2))
AC = math.hypot(float(a1) - float(c1), float(a2) - float(c2))
BC = math.hypot(float(b1) - float(c1), float(b2) - float(c2))
𝛼 = math.degrees(math.acos((AB ** 2 + AC ** 2 - BC ** 2)/ (2 * AB * AC)))
β = math.degrees(math.acos((AB ** 2 + BC ** 2 - AC ** 2)/ (2 * AB * BC)))
𝛾 = math.degrees(math.acos((AC ** 2 + BC ** 2 - AB ** 2)/ (2 * AC * BC)))
sys.stdout.write(str(𝛼) + '\n')
sys.stdout.write(str(β) + '\n')
sys.stdout.write(str(𝛾) + '\n')



