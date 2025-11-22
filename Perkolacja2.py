import numpy as np
import matplotlib.pyplot as plt
from collections import deque


L = 100
p = 0.59

def pbc(j, L):
    return j % L

def wyswietl_lattice(lattice, title=None):
    plt.imshow(lattice, cmap='magma', interpolation='nearest')
    plt.axis('off')
    if title is not None:
        plt.title(title)
    plt.show()

def leath_cluster(L, p):
    lattice = np.ones((L, L), dtype=int) * (-1)
    cluster = deque()

    for j in range(L):
        if np.random.random() < p:
            lattice[0, j] = 1
            cluster.append((0, j))
        else:
            lattice[0, j] = 0