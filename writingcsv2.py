# -*- coding: utf-8 -*-
"""
Created on Wed May 21 21:32:11 2025

@author: User
"""

#this is for pandas practise

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplcursors as mpl
plt.clf()

n = 100 # number of resistors
resval = 10 #resistor val
tolerance = 0.1 #10% tolerance

percenterr = np.random.uniform(-tolerance, tolerance, size = n)

vals = resval + (resval*percenterr)

df = pd.DataFrame({
    'resistor': [f'R{i+1}' for i in range(100)],
    'resistance/ohm': vals.round(2)
    })

df.to_csv('resistors.csv', index=False)

print(df.head())

#--------Stats-----------

# Want to plot a graph to get a nice view of the spread of results
# We then want to plot the standard deviation as we NEED precise resistors

df = pd.read_csv(r"C:\Users\User\Desktop\Python Projects\resistors.csv")
x = df["resistor"]
y = df['resistance/ohm']
#plt.plot(x,y,'b')
#plt.clf()
#y2 = []
#for i in range(0,100,1):
#    y2.append(95)
    
#y2 = [95] * len(x) # more elegant way of doing straight line
#plt.plot(x,y2,'r') # len(x), refers to the length of the x list

#y3 = [105] * len(x)
#plt.plot(x,y3,'r')
#y3 = []
#for i in range(0,100,1):
#    y3.append(105)
#plt.plot(x,y3,'r')

#df = df.mask(df['resistance/ohm']>105,np.nan) Makes the entire rows nans
#df = df.mask(df['resistance/ohm']<95,np.nan) Makes plotting impossible

df['resistance/ohm'] = df['resistance/ohm'].mask(df['resistance/ohm'] > 105, np.nan)
df['resistance/ohm'] = df['resistance/ohm'].mask(df['resistance/ohm'] < 95, np.nan)
df = df.dropna()
df.to_csv('resistorsnan.csv')

df = pd.read_csv(r"C:\Users\User\Desktop\Python Projects\resistorsnan.csv")
x2 = df["resistor"]
y2 = df["resistance/ohm"]
#plt.plot(x2,y2,'b')

y3 = [95] * len(x2) # more elegant way of doing straight line
#plt.plot(x2,y3,'r') # len(x), refers to the length of the x list

y4 = [105] * len(x2)
#plt.plot(x2,y4,'r')

#-----------standard deviation AFTER I've dropped resistances------------
plt.clf()
df = pd.read_csv(r"C:\Users\User\Desktop\Python Projects\resistors.csv")
x = df["resistor"]
y = df["resistance/ohm"]
s = np.std(y) #taking standard deviation
m = np.mean(y) #taking mean
print(s)
print("%3.2f" % m)

df['resistance/ohm'] = df['resistance/ohm'].mask(df['resistance/ohm'] >= m + s)
df['resistance/ohm'] = df['resistance/ohm'].mask(df['resistance/ohm'] <= m - s)
df = df.dropna()
df.to_csv('resistorsnan.csv')
ma = df['resistance/ohm'].max()
mi = df['resistance/ohm'].min()
x = df['resistor']
y = df['resistance/ohm']
y3 = [ma] * len(x)
y4 = [mi] * len(x)
plt.plot(x,y,'b')
fig, ax = plt.subplots()
line, = ax.plot(x, y, linestyle='-', marker=None, color='blue', label = "4.2")
cursor = mpl.cursor(line, hover=False)
plt.plot(x,y3,'r')
plt.plot(x,y4,'r')
print("max val is %3.2f" %ma)
print("min val is %3.2f" %mi)
plt.grid(True)
plt.tight_layout()
plt.legend(loc = "upper right", bbox_to_anchor=(1, 1), borderaxespad=0, facecolor = "white")
plt.minorticks_on() #grid minor code starts here
plt.grid(which='major', linestyle='-', linewidth=0.75, color='gray')
plt.grid(which='minor', linestyle='--', linewidth=0.5, color='lightgray')
#-----------------Plotting normal distribution---------------
