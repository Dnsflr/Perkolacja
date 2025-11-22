import numpy as np
import matplotlib.pyplot as plt
from collections import deque

def pbc(j, L):
    return j % L

def initialize_grid(L):
    lattice = np.ones((L, L)) * (-1)
    
            
