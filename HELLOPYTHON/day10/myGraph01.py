import numpy as np
import matplotlib.pyplot as plt

# make 3d axes
fig = plt.figure()
ax = fig.gca(projection='3d')

# test dataa
# x = np.arange(-1., 1., .1)
# y = np.arange(-1., 1., .1)

# 일반배열을 np배열로 바꿔준다
x = np.array([0, 0, 0, 0, 0])
y = np.array([0, 1, 2, 3, 4])
z = np.array([4, 1, 2, 3, 4])




print("x :", x)
print("y :", y)


# plot test data
ax.plot(x, y, z)
ax.plot(x+1, y, z)
ax.plot(x+2, y, z)

# make labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
