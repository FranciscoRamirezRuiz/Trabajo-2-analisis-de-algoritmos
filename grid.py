# grid.py

import random

def inicializar_grid(n):
    """
    Genera una cuadrícula de tamaño n x n con celdas aleatorias.
    - 'B' para bombas.
    - 'R' para cápsulas de RadAway.
    - '.' para celdas vacías.
    
    Args:
    n (int): Tamaño de la cuadrícula.

    Returns:
    list: La cuadrícula generada.
    """
    grid = [['.' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rand_val = random.choice(['.', 'B', 'R'])
            grid[i][j] = rand_val
    grid[0][0] = '.'  # La celda inicial es vacía
    grid[n-1][n-1] = '.'  # La celda final es vacía
    return grid
