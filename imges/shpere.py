import matplotlib.pyplot as plt
import numpy as np


class SphericalWalk:
    def __init__(self, num_points=10000, radius=1):
        self.num_points = num_points
        self.radius = radius
        self.x_vals = []
        self.y_vals = []
        self.z_vals = []

    def fill_walk(self):
        for _ in range(self.num_points):

            phi = np.arccos(2 * np.random.rand() - 1)
            theta = 2 * np.pi * np.random.rand()

            x = self.radius * np.sin(phi) * np.cos(theta)
            y = self.radius * np.sin(phi) * np.sin(theta)
            z = self.radius * np.cos(phi)

            self.x_vals.append(x)
            self.y_vals.append(y)
            self.z_vals.append(z)

    def plot_walk(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(self.x_vals, self.y_vals, self.z_vals, c='blue', s=1, alpha=0.6)

        ax.set_axis_off()

        plt.show()


sphere_walk = SphericalWalk(num_points=100000)
sphere_walk.fill_walk()
sphere_walk.plot_walk()
