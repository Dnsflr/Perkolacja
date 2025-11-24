import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import random

import matplotlib.animation as animation

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


def check_up_down(row_index,col_index):
    if ((lattice[row_index, col_index] == -1) and (lattice[row_index, col_index] != -2)):
        if (np.random.random() < p):
            lattice[row_index, col_index] = 1
            q.append([row_index, col_index])
        else:
            lattice[row_index, col_index] = 0
            
def check_sides(row_index,col_index):
    if (lattice[row_index, col_index] == -1):
        if (np.random.random() < p):
            lattice[row_index, col_index] = 1
            q.append([row_index, col_index])
        else:
            lattice[row_index, col_index] = 0
    
    
lattice = initialize_grid(L)

#anim
fig, ax = plt.subplots(figsize=(8, 8)) 
ax.set_title(f"Ewolucja (L={L}, p={p})")
frames = [] 

im_start = ax.imshow(lattice.copy(), interpolation='nearest', cmap='magma', animated=True)
frames.append([im_start])

licznik = 0
while q:
    row_index, col_index = q[0]
    
    #W dół 
    nr = row_index + 1
    nc = col_index
        
    check_up_down(nr, nc)
    
        
    #Na prawo
    nr = row_index
    nc = pbc(col_index + 1)
        
    check_sides(nr, nc)

    #Do góry 
    nr = row_index - 1
    nc = col_index
        
    check_up_down(nr, nc)
    
    #Lewo
    nr = row_index 
    nc = pbc(col_index - 1)
        
    check_sides(nr, nc)
    
    licznik += 1        
    SAVE_EVERY_N_STEPS = 25
     
    if licznik % SAVE_EVERY_N_STEPS == 0:
        im = ax.imshow(lattice.copy(), interpolation='nearest', cmap='magma', animated=True)
        frames.append([im])
        
    q.popleft()


im_final = ax.imshow(lattice.copy(), interpolation='nearest', cmap='magma', animated=True)
frames.append([im_final])

ani = animation.ArtistAnimation(fig, frames, interval=30, blit=True, repeat_delay=2000)

ani.save('ewolucja_perkolacji.gif', writer='pillow', fps=30)

plt.imshow(lattice, interpolation= 'nearest', cmap= 'magma')

plt.show()

plt.imshow(lattice, interpolation= 'nearest', cmap= 'magma')

plt.show()