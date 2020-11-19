#!/usr/bin/python3
# https://github.com/TianmingQu/Carol.git
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy.signal import find_peaks
# This part I am reading in the data and separate them into np.arrays
data = pd.read_csv('~/Desktop/2020fall programming course/bch5884-master/superose6_50.asc',skiprows = 3,delim_whitespace = True,nrows = 881).values
t = data [:,0] # t is for Time
L = data [:,1] # L is for absorbence
x = np.array(t)
y = np.array(L)
# I use find_peaks in scipy to find peaks and I set 50 as a threshold.
peak_id,peak_property = find_peaks(y, height = 50)
peak_t = x[peak_id]
peak_height = peak_property['peak_heights']
print('Peak apperance time is',peak_t)
print('peak_height is',peak_height)
dL = np.gradient(L) # Taking gradient for absorbence
# If the signal for gradient of i+1 and i-1 is different, then L[i] should be either the extreme point, and I take L[i] bigger than 50 as the threshold.
for i in range(2,879):
    if dL[i+1] * dL[i-1] < 0 and L[i] > 50 :
        if L[i] < L[i+1] and L[i] < L[i-1]: # extreme small point
            print(i)
            print(t[i])
# Find the beginning of the first peak and ending of the fourth peak
d = []
e = []
for i in range(2,376):
    a = dL[i+1] - dL[i]
    d.append(a)
d.index(max(d))

for i in range (520,879):
    if dL[i] <= 0.01: # I define the limit of slope by myself
        print(i)
print(list.index(min(mi)))

print('The first peak start at',t[361],'s','end at',t[386],'s')
print('The second peak start at',t[386],'s end at',t[421],'s')
print('The third peak start at',t[421],'s end at',t[516],'s')
print('The fourth peak start at',t[516],'s end at',t[571],'s')
plt.plot(x, y)
plt.show()
