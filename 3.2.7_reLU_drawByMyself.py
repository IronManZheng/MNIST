import numpy as np
import matplotlib.pylab as plt

def reLU_function_test(x):
    i = 0
    y = np.array(x) #array里面需要一个参数，这里目前只能放x，因为放其他的比如[1]的话，尺寸不对
    for i in range(len(x)):
        if x[i] > 0:
            y[i] = x[i]
            i += 1
        else:
            y[i] = 0
            i += 1
    return y

def reLU_function_byBook(x): #书上的例子
    return np.maximum(0,x)


x = np.arange(-5,5,0.1)
y = reLU_function_test(x)
plt.plot(x,y)
plt.show()