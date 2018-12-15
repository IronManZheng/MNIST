import numpy as np
import matplotlib.pylab as plt

def sigmoid_function_test(x):
    return 1/(1 + np.exp(-x))

x = np.arange(-5,5,0.1)
y = sigmoid_function_test(x)
plt.plot(x,y)
plt.show()