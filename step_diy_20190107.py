import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    y = x > 0
    y = y.astype(np.int)
    return y

x = np.arange(-5,5,0.1)
y = step_function(x)
plt.plot(x,y)
plt.show()