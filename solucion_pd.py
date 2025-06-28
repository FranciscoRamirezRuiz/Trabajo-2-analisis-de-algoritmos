# solucion_pd.py

def escape_tridimensional(mapa, n):
    """
    Resuelve el problema usando una tabla tridimensional de programación dinámica.
    """
    dp = [[[-1 for _ in range(2 * n)] for _ in range(n)] for _ in range(n)]

    def f(fila, columna, paso):
        if fila < 0 or fila >= n or columna < 0 or columna >= n or mapa[fila][columna] == 'B':
            return -1
        if paso == 2 * n - 1:
            return 0
        if dp[fila][columna][paso] != -1:
            return dp[fila][columna][paso]
        
        max_capsulas = max(
            f(fila + 1, columna, paso + 1),
            f(fila - 1, columna, paso + 1),
            f(fila, columna + 1, paso + 1),
            f(fila, columna - 1, paso + 1)
        )

        if mapa[fila][columna] == 'R':
            max_capsulas += 1

        dp[fila][columna][paso] = max_capsulas
        return max_capsulas

    return f(0, 0, 0)


def escape_hash(mapa, n):
    """
    Resuelve el problema usando una estructura hash (diccionario) para memorización.
    """
    hash_mem = {}

    def f(fila, columna, paso):
        if fila < 0 or fila >= n or columna < 0 or columna >= n or mapa[fila][columna] == 'B':
            return -1
        if paso == 2 * n - 1:
            return 0
        if (fila, columna, paso) in hash_mem:
            return hash_mem[(fila, columna, paso)]
        
        max_capsulas = max(
            f(fila + 1, columna, paso + 1),
            f(fila - 1, columna, paso + 1),
            f(fila, columna + 1, paso + 1),
            f(fila, columna - 1, paso + 1)
        )

        if mapa[fila][columna] == 'R':
            max_capsulas += 1

        hash_mem[(fila, columna, paso)] = max_capsulas
        return max_capsulas

    return f(0, 0, 0)
