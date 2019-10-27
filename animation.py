import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

from models import RoadMap, Roads, Lights

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

#plot nodes from csv file, traffic Lights


#colormap = np.array(['r', 'g', 'b'])
#categories = np.array([0, 2, 1, 1, 1, 2, 0, 0])

"""
t = np.linspace(0, 2 * np.pi, 15)
x = np.sin(t)
y = np.cos(t)
"""




plt.scatter(roads['stopx'], roads['stopy'], c='r')
#plt.scatter(roads['startx'], roads['starty'], s=100, c=y)

plt.scatter(roads['startx'], roads['starty'], s=100, c=color)



ax.add_patch(rect)

x = [(0,1), (0,0)]
y = [(1,1), (1,0)]

lines = []
for i in range(len(x)):
    hello, = ax.plot(x[i], y[i])
    lines.append(hello)

def init():
    global city, rect
    cars.set_data([], [])
    rect.set_edgecolor('none')
    for line in lines:
        line.set_ydata([np.nan] * len(x[1]))
    return cars, rect, lines[0], lines[1]

def animate(i):
    global city, rect, dt, ax, fig
    city.step(dt)

    rect.set_edgecolor('k')
    #particles.set_data(box.state[:, 0], box.state[:, 1])
    #particles.set_markersize(8)
    idx = 0
    for line in lines:
        line.set_ydata(y[idx])
        idx = idx+1

    cars.set_data(city.state[:, 0], city.state[:, 1])
    cars.set_markersize(8)
    return cars, rect, lines[0], lines[1]

ani = animation.FuncAnimation(fig, animate, frames=600,
                              interval=10, blit=True, init_func=init)

plt.show()
