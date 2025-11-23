import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import random

L = 100 
p = 0.59
q = deque()


def pbc(j):
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
    row_index, col_index = q[0]
    random_num = np.random.random()
    
        
    #Na prawo
    row_index = row_index
    col_index = pbc(col_index + 1)
        
    if (lattice[row_index, col_index] == -1):
        if (random_num < p):
            lattice[row_index, col_index] = 1
            q.append([row_index, col_index])
        else:
            lattice[row_index, col_index] = 0

    #Do góry 
    row_index = row_index + 1
    col_index = col_index
        
    if ((lattice[row_index, col_index] == -1) and (lattice[row_index, col_index] != -2)):
        if (random_num < p):
            lattice[row_index, col_index] = 1
            q.append([row_index, col_index])
        else:
            lattice[row_index, col_index] = 0
    
    
    q.popleft()
    

plt.imshow(lattice, interpolation= 'nearest', cmap= 'magma')

plt.show()