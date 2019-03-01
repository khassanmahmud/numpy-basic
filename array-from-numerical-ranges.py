import numpy as np

a = np.arange(5)
print('numpy.arange\n')
print(a)

# dtype set.
b = np.arange(5, dtype = float)
c = np.arange(5, dtype = np.float)
d = np.arange(5, dtype = int)
e = np.arange(5, dtype = np.int)

print(b)
print(c)
print(d)
print(e)

# Start and stop parameters set. 
f = np.arange(10, 20, 2)
g = np.arange(8, 50, 2)

print(f)
print(g)

h = np.linspace(10, 20, 5)
i = np.linspace(10, 20, 5, endpoint = True)

# endpoint set to false.
j = np.linspace(10, 20, 5, endpoint = False)

print('\nnumpy.linspace\n')
print(h)
print(i)
print(j)

# Find retstep value.
k = np.linspace(1, 2, 5, retstep = True) 
print(k)

# Default base is 10.
l = np.logspace(1.0, 2.0, num = 10)
print('\nnumpy.logspace\n')
print(l)

# Set base of log space to 2.
m = np.logspace(1, 10, num = 10, base = 2)
print(m)