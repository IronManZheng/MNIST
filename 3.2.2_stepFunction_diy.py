import numpy as np

def step_function(x):
    i = 0
    y = np.arange(len(x))
    for i in range(len(x)):
        if x[i] <= 0:
            y[i] = 0
        else:
            y[i] = 1
        i+=1
    return y

x = [-0.5,0.5,0.6]
result = step_function(x)
print(result)
