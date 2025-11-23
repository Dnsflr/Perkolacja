import numpy as np
import matplotlib.pyplot as plt
from collections import deque

L = 20 
p = 0.59


def pbc(j, L):
    return j % L

def initialize_grid(L):
    lattice = np.ones((L, L)) * (-1)
    
    #brzegi
    lattice[0,:] = -2
    lattice[-1,:] = -2
    
    
    return lattice
    


lattice = initialize_grid(L)

for i in range(L):
    for j in range(L):
        pass


plt.imshow(lattice, interpolation= 'nearest', cmap= 'magma')

plt.show()