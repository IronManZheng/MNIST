import numpy as np

array_a = np.array([1.534,2.897,0.384])
print("array_a:")
print(array_a)
exp_a = np.exp(array_a)
print("exp_a:")
print(exp_a)
sum_a = np.sum(exp_a)
print("sum_a:")
print(sum_a)
result = exp_a/sum_a

print(result)