import numpy.matlib
import numpy as np

# Filled with random data.
print('np.matlib.empty():\n')
print(np.matlib.empty((2, 2)))

# Filled with zeros.
print('\nnp.matlib.zeros():\n')
print(np.matlib.zeros((2, 2)))

# Filled with ones.
print('\nnp.matlib.ones():\n')
print(np.matlib.ones((2, 2)))

# numpy.matlib.eye()
print('\nnp.matlib.eye():\n')
print(np.matlib.eye(n = 3, M = 4, k = 0, dtype = float))

# numpy.matlib.identity()
print('\nnp.matlib.identity():\n')
print(np.matlib.identity(5, dtype = float))

# numpy.matlib.rand()
print('\nnp.matlib.rand():\n')
print(np.matlib.rand(3, 3))

# numpy.matrix()
i = np.matrix('1,2;3,4')
print('\nnp.matrix():\n')
print(i)

j = np.asarray(i)
print('\nnp.asarray():\n')
print(j)

k = np.asmatrix(j)
print('\nnp.asmatrix():\n')
print(k)