from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.gca(projection = '3d')
x = np.arange(-4, 4, 0.1)
y = np.arange(-4, 4, 0.1)
x, y = np.meshgrid(x, y)
z = 0

K = 0
c = 0.01

a = [[-2, -2], [0, -2], [2,-2]]


n = np.arange(3)
for i in n:
    z = z + ((x - a[i][0])**2 + (y - a[i][1])**2 + c)**(-1)
z = K - z
surf = ax.plot_surface(x, y, z, cmap = plt.cm.coolwarm)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Sekelova funkcija')
fig.colorbar(surf)
plt.show()