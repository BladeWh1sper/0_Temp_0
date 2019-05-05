
#%%
print("Hello World")


#%%
import time
time.sleep(3)


#%%
def say_hello(recipient):
    return 'Hello, {}!'.format(recipient)

say_hello('Tim')


#%%
import numpy as np

def square(x):
    return x * x


#%%
x = np.random.randint(1, 10)
y = square(x)

print('%d squared is %d' % (x, y))


#%%
x = np.random.randint(1, 10)
y = square(x)

print('%d squared is %d' % (x, y))


#%%



