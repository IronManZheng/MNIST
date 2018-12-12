import numpy as np
import matplotlib.pylab as plt

x = np.arange(-5,5,0.1,complex)
y = 2 * x
z = 3 * x
plt.plot(x,y)
plt.plot(x,z)
plt.xlim(-2,2)
plt.ylim(-5,5)
plt.show()

