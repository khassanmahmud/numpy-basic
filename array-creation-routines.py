import numpy as np

a = np.empty([3, 2], dtype = int)

print 'numpy.empty\n'
print a

# Array of five zeros. Default dtype is float. 
b = np.zeros(5)
c = np.zeros((5,), dtype = np.float)
d = np.zeros((5,), dtype = float)
e = np.zeros((5,), dtype = np.int)
f = np.zeros((5,), dtype = int)

# Custom type.
g = np.zeros((2, 2), dtype = [('x', 'i4'), ('y', 'i4')])

print '\nnumpy.zeros\n'
print b
print c
print d
print e
print f
print g

# Array of five ones. Default dtype is float. 
h = np.ones(5)
i = np.ones((5,), dtype = np.int)
j = np.ones((5,), dtype = int)
k = np.ones([2, 2], dtype = int)

print '\nnumpy.ones\n'
print h
print i
print j
print k