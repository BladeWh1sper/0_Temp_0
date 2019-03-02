import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
text_file = open("web_traffic.txt", "r")
performance = text_file.read().split("\n")
performance = list(map(int, performance))
print (performance)


plt.bar(y_pos, performance, align='center', alpha=1)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
 
plt.show()
