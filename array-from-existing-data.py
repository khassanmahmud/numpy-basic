import numpy as np

x = [1, 2, 3]
y = (1, 2, 3)
z = [(1, 2, 3), (4, 5)]
s = 'Hello World'

# Convert list to ndarray. 
a = np.asarray(x)

print('ndarray from List\n')
print(a)

# dtype is set.
b = np.asarray(x, dtype = float)
c = np.asarray(x, dtype = np.float)
d = np.asarray(x, dtype = int)
e = np.asarray(x, dtype = np.int)

print(b)
print(c)
print(d)
print(e)

f = np.asarray(y)

print('\nndarray from Tuple\n')
print(f)

# ndarray from list of tuples. 
g = np.asarray(z)
print(g)

h = np.frombuffer(s, dtype = 'S1')
print(h)

# Create list object using range function.
list = range(5)
print(list)

# Obtain iterator object from list. 
it = iter(list)

# Use iterator to create ndarray. 
i = np.fromiter(it, dtype = float)
j = np.fromiter(it, dtype = np.float)
k = np.fromiter(it, dtype = int)
l = np.fromiter(it, dtype = np.int)

print(i)
print(j)
print(k)
print(l)