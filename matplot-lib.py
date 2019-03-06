import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1, 11)
y = 2 * x + 5

plt.title("Matplotlib demo")
plt.xlabel("X - axis caption")
plt.ylabel("Y - axis caption")
plt.plot(x, y)
plt.show()

x = np.arange(1, 11)
y = 2 * x + 5

plt.title("Matplotlib demo")
plt.xlabel("X - axis caption")
plt.ylabel("Y - axis caption")
plt.plot(x, y, "ob")
plt.show()

# Sine Wave Plot:
# Compute the x and y coordinates for points on a sine curve. 
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

plt.title("Sine wave form")
plt.plot(x, y)
plt.show()

# subplot()
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Set up a subplot grid that has height 2 and width 1, 
# and set the first such subplot as active. 
plt.subplot(2, 1, 1)

# Make the first plot.
plt.plot(x, y_sin)
plt.title("Sine")

# Set the second subplot as active, and make the second plot.
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title("Cosine")

plt.show()

# bar()
x = [5, 8, 10]
y = [12, 16, 6]

x2 = [6, 9, 11]
y2 = [6, 15, 7]

plt.bar(x, y, align = "center")
plt.bar(x2, y2, color = "g", align = "center")
plt.title("Bar graph")
plt.ylabel("Y - Axis")
plt.xlabel("X - Axis")
plt.show()