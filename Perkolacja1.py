import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import random

L = 100 
p = 0.59
q = deque()

# pomocnicza globalna zmienna na losowanie
random_num = 0.0


def pbc(j):
    return j % L


def initialize_grid(L_local):
    global q
    lattice_local = np.ones((L_local, L_local)) * (-1)
    
    lattice_local[0, :] = -2
    lattice_local[-1, :] = -2
    lattice_local[1, :] = 1

    q = deque()
    for i in range(L_local):
        for j in range(L_local):
            if i == 1:
                q.append([i, j])

    return lattice_local


def check_up_down(row_index,col_index):
    if ((lattice[row_index, col_index] == -1) and (lattice[row_index, col_index] != -2)):
        if (random_num < p):
            lattice[row_index, col_index] = 1
            q.append([row_index, col_index])
        else:
            lattice[row_index, col_index] = 0
            
def check_sides(row_index,col_index):
    if (lattice[row_index, col_index] == -1):
        if (random_num < p):
            lattice[row_index, col_index] = 1
            q.append([row_index, col_index])
        else:
            lattice[row_index, col_index] = 0


def leath_once(L_local, p_local):
    global L, p, lattice, q, random_num

    L = L_local
    p = p_local

    lattice = initialize_grid(L)

licznik = 0 
while q:
    row_index, col_index = q[0]
    random_num = np.random.random()
    
    #W dół 
    row_index = row_index + 1
    col_index = col_index
        
    check_up_down(row_index, col_index)
    
        
    #Na prawo
    row_index = row_index
    col_index = pbc(col_index + 1)
        
    check_sides(row_index, col_index)

    #Do góry 
    row_index = row_index - 1
    col_index = col_index
        
    check_up_down(row_index, col_index)
    
    #Lewo
    row_index = row_index 
    col_index = pbc(col_index - 1)
        
    check_sides(row_index, col_index)
            
            
    q.popleft()
    

plt.imshow(lattice, interpolation= 'nearest', cmap= 'magma')

plt.show()
