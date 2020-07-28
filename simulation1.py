import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

degreespeed = .1


def animate(i):
    global degreespeed
    graph_data = open('data.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x) + degreespeed)
            ys.append(float(y) + degreespeed)
    ax1.clear()
    ax1.scatter(xs, ys, label='skitscat', color='k', s=25, marker="o")
    degreespeed += degreespeed * .1


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
