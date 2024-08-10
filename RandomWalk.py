from random import choice
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_vals = [0]
        self.y_vals = [0]

    def fill_walk(self):
        while len(self.x_vals) < self.num_points:
            x_dir = choice([-1, 1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_dir * x_distance

            y_dir = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_dir * y_distance

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_vals[-1] + x_step
            y = self.y_vals[-1] + y_step

            self.x_vals.append(x)
            self.y_vals.append(y)


while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))

    point_numbers = range(rw.num_points)
    ax.plot(rw.x_vals, rw.y_vals, linewidth=1, color='blue')

    ax.plot(0, 0, c='green', edgecolors='none', s=100)
    ax.plot(rw.x_vals[-1], rw.y_vals[-1], c='red', edgecolors='none', s=100)

    ax.axis('off')

    plt.show()

    keep_running = input("Do you want to plot another walk (y/n): ")
    if keep_running.lower() == 'n':
        break
