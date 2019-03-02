from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
style.use("ggplot")

x,y = np.loadtxt("web_traffic.txt", unpack = True, delimiter = ",")

plt.plot(x,y)
plt.title("Chart")
plt.ylabel("Y axis")
plt.xlabel("X axis")

plt.show()