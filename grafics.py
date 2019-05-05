import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
objects = ('Python', 'C++', 'Java')
y_pos = np.arange(len(objects))
"""
text_file = open("web_traffic.txt", "r")
performance = text_file.read().split("\n")
performance = list(map(int, performance))
print (performance)
"""
with open('web_traffic.txt') as f:
    lines = f.readlines()
    x = [line.split(", ")[0] for line in lines]
    y = [line.split(", ")[1] for line in lines]
    z = [line.split(", ")[2] for line in lines]
x = list(map(int, x))
x = sum(x)
y = list(map(int, y))
y = sum(y)
z = list(map(int, z))
z = sum(z)
performance = [x, y, z]

plt.bar(y_pos, performance, align='center', alpha=1)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
 
plt.show()
