# generar_mapa.py

import random

def generar_mapa(n):
    """
    Genera un mapa de tamaño n x n con celdas aleatorias:
    - 'B' para bombas.
    - 'R' para cápsulas RadAway.
    - '.' para celdas vacías.
    """
    mapa = [['.' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            valor = random.choice(['.', 'B', 'R'])
            mapa[i][j] = valor
    mapa[0][0] = '.'          # Celda inicial siempre vacía
    mapa[n-1][n-1] = '.'      # Celda final siempre vacía
    return mapa
