import numpy as np

def softmax_function(a):
    a_max = np.max(a)
    return np.exp(a - a_max)/np.sum(np.exp(a - a_max))

a = np.array([1010,1000,990])
out = softmax_function(a)
out_sum = np.sum(out)
print(out)
print(out_sum)