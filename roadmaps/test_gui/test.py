
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
# Initializing number of dots
N = 25
XC = 5
YC = 5
R = 1
R_SQR = R **2

# Creating dot class
class dot(object):
    def __init__(self, ind):
        self.x = 10 * np.random.random_sample()
        self.y = 10 * np.random.random_sample()
        self.velx = self.generate_new_vel()
        self.vely = self.generate_new_vel()
        self.in_circle = not self.calc_out_of_circle()

    def generate_new_vel(self):
        return (np.random.random_sample() - 0.5) / 5

    def move(self) :
        if np.random.random_sample() < 0.95:
            self.check_out_of_circle()
            self.x += self.velx
            self.y += self.vely
        else:
            self.velx = self.generate_new_vel()
            self.vely = self.generate_new_vel()
            self.check_out_of_circle()
            self.x += self.velx
            self.y += self.vely
        self.check_inside_circle()

    def calc_out_of_circle_with_params(self, x, y):
        return (x - XC) ** 2 + (y - YC) ** 2 >= R_SQR ** 2

    def calc_out_of_circle(self):
        return self.calc_out_of_circle_with_params(self.x, self.y)

    def check_out_of_circle(self):
        if self.in_circle and self.calc_out_of_circle_with_params(self.x + self.velx, self.y + self.vely):
            self.velx = -self.velx
            self.vely = -self.vely

    def check_inside_circle(self):
        if not self.calc_out_of_circle():
            self.in_circle = True


# Initializing dots
dots = [dot(i) for i in range(N)]

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
d, = ax.plot([dot.x for dot in dots],
             [dot.y for dot in dots], 'ro', markersize=3)
circle = plt.Circle((XC, YC), R, color='b', fill=False)
ax.add_artist(circle)


# animation function.  This is called sequentially
def animate(i):
    for dot in dots:
        dot.move()
    d.set_data([dot.x for dot in dots],
               [dot.y for dot in dots])
    return d,

# call the animator.
anim = animation.FuncAnimation(fig, animate, frames=200, interval=20)
# plt.axis('equal')
plt.show()