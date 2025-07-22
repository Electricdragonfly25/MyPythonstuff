# -*- coding: utf-8 -*-
"""
Created on Fri May 23 21:19:39 2025

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#------writing dataset----------

df = pd.DataFrame({
    "time/hour": [10,11,12,13,14,15,16,17,18,19,20],
    "temp/degrees": [22.1,23,23.7,30,25,20,21,23,23.6,22.9,22.4],
    "temp/degrees2": [24,23,22,23,24,22,34,21,22,22,23]
    })

df.to_csv(r'C:\Users\User\Desktop\temps.csv', index = False)

#-------reading dataset---------------

opensesame = pd.read_csv(r'C:\Users\User\Desktop\temps.csv')

print(opensesame)

opensesame = df[['time/hour','temp/degrees']]
print(opensesame)

#--------plotting basic graph------------ whoopsie code--------------

#xpoints = 
#ypoints = 
#plt.plot[xpoints,ypoints]
#plt.show()

#--------plotting basic graph using CSV--- Sheffield code and playing with plot--------------

#df = pd.read_csv(r'C:\Users\User\Desktop\temps.csv')

#df.plot.scatter('time/hour','temp/degrees')

#x = df['time/hour']
#y = df['temp/degrees']
#plt.plot(x,y,'r')
# Force x-axis ticks to show every hour
#plt.xticks(list(range(10, 21)))  # includes 10 through 20
#plt.xlim(10,20)
#plt.ylim(18,35)
#plt.xlabel("time/hour", fontsize = 14)
#plt.ylabel("Temperature/degrees C", fontsize = 14)
#plt.title("Me graph", fontsize = 18)
#plt.xticks(fontsize = 14)
#plt.yticks(fontsize = 14)
#plt.grid(True)
#plt.tight_layout()
#plt.minorticks_on() #grid minor code starts here
#plt.grid(which='major', linestyle='-', linewidth=0.75, color='gray')
#plt.grid(which='minor', linestyle='--', linewidth=0.5, color='lightgray')
#plt.show() #clears everything that came before, the figure basically resets

#x = df['time/hour']
#y = df['temp/degrees2']
#plt.plot(x,y,'b')

#------------------PhD data--------------------------

#df = pd.read_csv(r"C:\Users\User\Documents\S11DIVSMALL.csv")
plt.clf()
plt.subplot(2,1,1)
x = pd.read_csv(r'E:\Lab results\chamber results 07022023 YES nodis\sqloop.csv', usecols=[0], skiprows=3, nrows=801)
y1 = pd.read_csv(r'E:\Lab results\chamber results 07022023 YES nodis\sqloop.csv', usecols=[1], skiprows=3, nrows=801)
x = x/1e+09
plt.plot(x,y1,'b', label = "sqloop")
x = pd.read_csv(r'E:\Lab results\chamber results 07022023 YES nodis\patchdis2door.csv', usecols=[0], skiprows=3, nrows=801)
y2 = pd.read_csv(r'E:\Lab results\chamber results 07022023 YES nodis\patchdis2door.csv', usecols=[1], skiprows=3, nrows=801)
x = x/1e+09
plt.plot(x,y2,'r', label = "patchdis2door")
plt.xlim(1.5, 8)
ticks = np.linspace(1.5,8, num = 14) #writing in ticks and num specifies the number of ticks :)
plt.xticks(ticks)
#plt.xticks(list(range(1.5, 8)))
#plt.ylim(0,-50)
plt.grid(True)
plt.tight_layout()
plt.minorticks_on() #grid minor code starts here
plt.grid(which='major', linestyle='-', linewidth=0.75, color='gray')
plt.grid(which='minor', linestyle='--', linewidth=0.5, color='lightgray')
plt.legend(loc = "upper right", bbox_to_anchor=(1, 1), borderaxespad=0, facecolor = "white")
plt.xlabel("Frequency/GHz")
plt.ylabel("S parameter magnitude/dB")
plt.title('Reflectivity results')

"""plt.subplot(2,1,2)
x = pd.read_csv(r'E:\Lab results\chamber results 07022023 YES nodis\sqloop.csv', usecols=[0], skiprows=3, nrows=801)
y = pd.read_csv(r'E:\Lab results\chamber results 07022023 YES nodis\sqloop.csv', usecols=[1], skiprows=3, nrows=801)
x = x/1e+09
plt.plot(x,y,'b')
plt.xlim(1.5, 8)
ticks = np.linspace(1.5,8, num = 14) #writing in ticks
plt.xticks(ticks)
#plt.xticks(list(range(1.5, 8)))
#plt.ylim(0,-50)
plt.grid(True)
plt.tight_layout()
plt.minorticks_on() #grid minor code starts here
plt.grid(which='major', linestyle='-', linewidth=0.75, color='lightgray')
plt.grid(which='minor', linestyle='--', linewidth=0.5, color='lightgray')
plt.xlabel("Frequency/GHz")
plt.ylabel("S parameter magnitude/dB")
#x = df['Frequency']
#y = df['Formatted Data']
#plt.plot(x,y,'b')"""