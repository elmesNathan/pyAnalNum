import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math

matrice = [
	[5, 10, 15],
	np.linspace(0,1,2000),
	[15, 10, 5]
]

def calotte(m):
	fnc = []
	for i in m[1]:
		fnc.append(math.sqrt(1-(i**2)))
	return fnc
fig = plt.figure()
func = calotte(matrice)
print(func)
plt.figure()

def update(i):
    fx.plt.plot(i)
    return [fx]

anim = FuncAnimation(
	fig, 
	update, 
	frames=func, 
	interval=200
	)

plt.show()
