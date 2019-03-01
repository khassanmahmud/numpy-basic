import numpy as np

# Using array-scalar type. 
dt1 = np.dtype(np.int32)

# int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2', 'i4', etc. 
dt2 = np.dtype('i4')

# Using endian notation. 
dt3 = np.dtype('>i4')

# First create structured data type. 
dt4 = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype = dt4)

student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
b = np.array([('John Doe', 21, 50), ('William Clark', 18, 75)], dtype = student)

print(dt1)
print(dt2)
print(dt3)

print(dt4)
print(a)
print(a['age'])

print(student)
print(b)
print(b['name'])
print(b['age'])
print(b['marks'])