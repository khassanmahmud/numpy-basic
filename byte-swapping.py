import numpy as np

a = np.array([1, 256, 8755], dtype = np.int16)

print('\nMain array:\n')
print(a)

print('\nRepresentation of data in memory in hexadecimal form:\n') 
print(map(hex, a))

print('\nApplying byteswap() function:\n') 
print(a.byteswap(True))

print('\nIn hexadecimal form:\n') 
print(map(hex, a))
