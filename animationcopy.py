import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

from models import RoadMap, Roads, Lights

#data
roads = pd.read_csv('fake_data.csv')
init_state = []
NUM_CARS = 20
#for _ in range(NUM_CARS):
    # print(roads.iloc[0]['Start'])

# [x, y, vx, vy]
init_state = [[0,1,1,0], [1,1,0,1], [1,1,-1,0],[-1,-1,1,0],[-2,-1,0,1]]

city = RoadMap(init_state, size=0.04)
dt = 1. / 50
#============================================================#
fig = plt.figure()
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(-10.2, 10.2), ylim=(-10.4, 10.4))

cars, = ax.plot([], [], 'bo', ms=6)

rect = plt.Rectangle(city.bounds[::2],
                     city.bounds[1] - city.bounds[0],
                     city.bounds[3] - city.bounds[2],
                     ec='none', lw=2, fc='none')

#plot nodes from csv file
plt.scatter(roads['stopx'], roads['stopy'], color='g')
plt.scatter(roads['startx'], roads['starty'], color='b')

ax.add_patch(rect)
x = (0,1)
y = (0,1)
line, = ax.plot(x, y)

def init():
    global city, rect
    cars.set_data([], [])
    rect.set_edgecolor('none')
    line.set_ydata([np.nan] * len(x))
    return cars, rect, line

def animate(i):
    global city, rect, dt, ax, fig
    city.step(dt)

    rect.set_edgecolor('k')
    #particles.set_data(box.state[:, 0], box.state[:, 1])
    #particles.set_markersize(8)

    line.set_ydata(y)

    cars.set_data(city.state[:, 0], city.state[:, 1])
    cars.set_markersize(8)
    return cars, rect, line

ani = animation.FuncAnimation(fig, animate, frames=600,
                              interval=10, blit=True, init_func=init)

plt.show()
