# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import matplotlib.patches as mpatches
 
# y-axis in bold
rc('font', weight='bold')

with open('web_traffic.txt') as f:
    lines = f.readlines()
    l = [line.split(",")[0] for line in lines]
    x = [line.split(",")[1] for line in lines]
    y = [line.split(",")[2] for line in lines]
    z = [line.split(",")[3] for line in lines]
    n = [line.split(",")[4] for line in lines]
x = list(map(int, x))
x = sum(x)
y = list(map(int, y))
y = sum(y)
z = list(map(int, z))
z = sum(z)
n = list(map(int, n))
n = sum(n)



bars1 = [x, y, z]
bars2 = [n, 7, 16]
bars3 = [25, 3, 23]
 
bars = np.add(bars1, bars2).tolist()
 
r = [0,1,2]
 
names = l
barWidth = 1
 
p1a = plt.bar(r, bars1, color='#7f6d5f', edgecolor='white', width=barWidth)

p1b = plt.bar(r, bars2, bottom=bars1, color='#557f2d', edgecolor='white', width=barWidth)

p1c = plt.bar(r, bars3, bottom=bars, color='black', edgecolor='white', width=barWidth)

plt.xticks(r, names, fontweight='bold')
plt.xlabel("group")

plt.legend([p1a, p1b, p1c, (p1a, p1b, p1c)], ["sda", "dad", "dasda"])
 

plt.show()

