import numpy as np
import matplotlib.pyplot as plt
from collections import deque

def run_leath_simulation(L, p):
    is_open = np.random.random((L, L)) < p
    
    visited = np.zeros((L, L), dtype=int)
    
    q = deque()
    
    start_row = 1
    cluster_size = 0
    
    for j in range(L):
        if is_open[start_row, j]:
            visited[start_row, j] = 1
            q.append((start_row, j))
            cluster_size += 1
        else:
            visited[start_row, j] = -1 

    percolates = False
    
    # Wektory przesunięć: Dół, Góra, Prawo, Lewo
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        r, c = q.popleft() 

        if r == L - 2:
            percolates = True
        
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            
            nc = nc % L 

            if 0 < nr < L - 1:
                if visited[nr, nc] == 0:
                    if is_open[nr, nc]:
                        visited[nr, nc] = 1 
                        cluster_size += 1
                        q.append((nr, nc))
                    else:
                        visited[nr, nc] = -1 
    
    return percolates, cluster_size


L_values = [20, 50, 100] 
p_values = np.arange(0, 1, 0.1) 
n_samples = 100 


P_results = {L: [] for L in L_values} # P(p)
S_results = {L: [] for L in L_values} # S(p)



for L in L_values:
    for p in p_values:
        perc_count = 0
        non_perc_sizes = []
        
        for _ in range(n_samples):
            is_perc, size = run_leath_simulation(L, p)
            
            if is_perc:
                perc_count += 1
            else:
                non_perc_sizes.append(size)
        

        P_p = perc_count / n_samples
        P_results[L].append(P_p)
        

        if len(non_perc_sizes) > 0:
            avg_size = np.mean(non_perc_sizes)
            S_results[L].append(avg_size / (L**2)) 
        else:
            S_results[L].append(0)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))


for L in L_values:
    ax1.plot(p_values, P_results[L], label=f'L={L}')
ax1.set_title('P(p) - Prawdopodobieństwo perkolacji')
ax1.set_xlabel('p - koncentracja')
ax1.set_ylabel('P - percolation probability')
ax1.legend()
ax1.grid(True)


for L in L_values:
    ax2.plot(p_values, S_results[L], label=f'L={L}')
ax2.set_title('S(p)/L^2 - Średni rozmiar klastra nieperkolacyjnego')
ax2.set_xlabel('p - koncentracja')
ax2.set_ylabel('S / L^2')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()