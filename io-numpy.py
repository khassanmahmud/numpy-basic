import numpy as np

a = np.array([1, 2, 3, 4, 5])

np.save("outfile", a)
b = np.load("outfile.npy")
print(b)

np.savetxt("out.txt", a)
c = np.loadtxt("out.txt")
print(c)