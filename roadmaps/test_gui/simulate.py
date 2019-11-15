import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from models import RoadMap

# [x, y, vx, vy]
init_state = [[-8,0,1,0], [-8,-8,1,0], [-8,6,1,0],[-8,-4,1,0],[-8,-2,1,0]]

city = RoadMap(init_state, size=0.04)
dt = 1. / 20
#============================================================#
fig = plt.figure()
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(-10.2, 10.2), ylim=(-10.4, 10.4))

# Draw the grid
for i in range(-10, 11, 2):
  ax.axhline(y=i)
for i in range(-10, 11, 2):
  ax.axvline(x=i)


# Draw the lights
lights = []
for j in range(-10, 11, 2):
  x_range = list(range(-10, 11, 2))
  if j == 4 or j == 2:
    lights.append(ax.scatter(x_range, [j]*len(x_range), color='red'))
  else:
    lights.append(ax.scatter(x_range, [j]*len(x_range), color='g'))



cars, = ax.plot([], [], 'bo', ms=6)

rect = plt.Rectangle(city.bounds[::2],
                     city.bounds[1] - city.bounds[0],
                     city.bounds[3] - city.bounds[2],
                     ec='none', lw=2, fc='none')

#plot nodes from csv file
# plt.scatter(roads['stopx'], roads['stopy'], color='g')
# plt.scatter(roads['startx'], roads['starty'], color='b')

ax.add_patch(rect)
def init():
    global city, rect
    cars.set_data([], [])
    rect.set_edgecolor('none')
    return cars, rect

def animate(i):
    global city, rect, dt, ax, fig, lights
    city.step(dt)

    rect.set_edgecolor('k')

    cars.set_data(city.state[:, 0], city.state[:, 1])
    cars.set_markersize(8)
    return cars, rect

ani = animation.FuncAnimation(fig, animate, frames=600,
                              interval=10, blit=True, init_func=init)

plt.show()
