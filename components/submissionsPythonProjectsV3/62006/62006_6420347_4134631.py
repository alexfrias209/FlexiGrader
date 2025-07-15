# 93 - Random Walk Simulator (Paul Catam, Lab 05L)

import numpy as np
import matplotlib.pyplot as plt
# importing two libraries for the graph


def random(steps):
    x = np.zeros(steps)
    y = np.zeros(steps)
    # defining the x and y positions of the walk

    for i in range(1, steps):       #loop between 1 to value of steps
        angle = np.random.uniform(0, 2 * np.pi) # random angle from 0-2 times pi
        x[i] = x[i - 2] + np.cos(angle) 
        y[i] = y[i - 2] + np.sin(angle)
        # movement of the walk in the x and y axis

    return x, y

def walk(x, y):
    plt.plot(x, y, marker='s')
    # change the shape of the marker with x, o, s, p, etc.
    
    plt.title("2D Random Walk")
    plt.xticks([])  # hides the x axis (for aesthetic)
    plt.yticks([])  # hides the y axis (for aesthetic)
    plt.show()      #displays the graph/walk 

if __name__ == "__main__":
    steps = 50  # number of steps 
    x, y = random(steps)    
    walk(x, y)
    # executes 2D random walk

# FOR EVERY NEW RUN, A RANDOM WALKING PLOT IS DISPLAYED
