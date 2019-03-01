import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

c = a * b

print(c)

d = np.array([[0.0, 0.0, 0.0], [10.0, 10.0, 10.0], [20.0, 20.0, 20.0], [30.0, 30.0, 30.0]])
e = np.array([1.0, 2.0, 3.0])

print('\nFirst array:\n')
print(d)
print('\nSecond array:\n')
print(e)
print('\nArray after broadcasitng:\n')
print(d + e)