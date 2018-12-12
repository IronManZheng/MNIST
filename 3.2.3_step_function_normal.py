import numpy as np
import matplotlib.pylab as plt

def step_function(x): #use a few steps that designed by myself
    y = x > 0
    print("y:")
    y = y.astype(np.int)
    return y

def step_fuction_easy(x): #This describ style is written by the book
    return np.array(x > 0,dtype=np.int)

x = np.arange(-2,2,0.1)
#y = step_function(x)  #use the fuction that designed by myselfS
y = step_fuction_easy(x) #use the function that designed by the book
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()