import numpy as np

def step_function(x):
    y = x > 0
    y = y.astype(np.int)
    return y

x = np.array([-0.5,0.6,1.2])
result = step_function(x)
print(result)