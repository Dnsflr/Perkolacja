import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import random

L = 20 
p = 0.59
q = deque()


def pbc(j, L):
    return j % L

def initialize_grid(L):
    lattice = np.ones((L, L)) * (-1)
    
    #brzegi
    lattice[0,:] = -2
    lattice[-1,:] = -2
    lattice[1,:] = 1
    
    for i in range(L):
        for j in range(L):
            if i == 1:
                q.append([i,j])
            else:
                pass
    
    return lattice
    
lattice = initialize_grid(L)

licznik = 0 
while q:
    x_index, y_index = q[0]
    
    for i in range(4):
        if (lattice[x_index, pbc(y_index + 1)] != -1):
            pass
    
    q.popleft()
    

plt.imshow(lattice, interpolation= 'nearest', cmap= 'magma')

plt.show()