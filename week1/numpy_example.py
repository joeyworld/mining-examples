import numpy as np

a = np.arange(9)
print(a)
print(type(a))

a = a.reshape((3, 3))
print(a)

b = np.arange(9).reshape((3, 3))
print(b)
print(a * b)
