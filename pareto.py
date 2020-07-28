import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random
from random import choice
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
x1 = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars
fig, ax = plt.subplots()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


wealth = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]


def pareto():

    for x in range(0, 9):
        for y in range(0, 9):
            if x == y:
                continue

            flip = random.randint(0, 1)
            if wealth[x] == 0 or wealth[y] == 0:
                continue

            if flip == 1:
                wealth[x] += 1
                wealth[y] -= 1
            wealth.sort(reverse=True)


def animate(i):
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('wealth')
    ax.set_title('person')
    ax.set_xticks(x1)
    ax.set_xticklabels(labels)
    ax.legend()
    ax.clear()
    pareto()

    rects = ax.bar(x1 - width/2, wealth, width, label='Wealth')
    autolabel(rects)
    fig.tight_layout()


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
