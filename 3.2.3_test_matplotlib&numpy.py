import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    y = x > 0
    print("y:")
    y = y.astype(np.int)
    return y

x = np.arange(-2,2,0.1)
y = step_function(x)
plt.plot(x,y)
plt.show()