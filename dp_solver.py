# dp_solver.py

def escape_tridimensional(grid, n):
    """
    Resuelve el problema usando una tabla tridimensional de programación dinámica.

    Args:
    grid (list): La cuadrícula del refugio.
    n (int): Tamaño de la cuadrícula.

    Returns:
    int: El máximo número de cápsulas que se pueden recoger.
    """
    dp = [[[-1 for _ in range(2 * n)] for _ in range(n)] for _ in range(n)]

    def f(x, y, t):
        if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] == 'B':
            return -1  # Si estamos fuera del rango o en una bomba, no es válido
        if t == 2 * n - 1:
            return 0  # Casos base: hemos llegado al límite de pasos
        if dp[x][y][t] != -1:
            return dp[x][y][t]  # Devuelve el valor memoizado

        # Evaluamos las cuatro posibles direcciones
        max_capsulas = max(f(x + 1, y, t + 1), f(x - 1, y, t + 1),
                           f(x, y + 1, t + 1), f(x, y - 1, t + 1))

        # Si hay una cápsula en esta celda, sumamos 1
        if grid[x][y] == 'R':
            max_capsulas += 1

        dp[x][y][t] = max_capsulas
        return max_capsulas

    return f(0, 0, 0)


def escape_hash(grid, n):
    """
    Resuelve el problema usando un diccionario hash para memorización.

    Args:
    grid (list): La cuadrícula del refugio.
    n (int): Tamaño de la cuadrícula.

    Returns:
    int: El máximo número de cápsulas que se pueden recoger.
    """
    dp = {}

    def f(x, y, t):
        if x < 0 or x >= n or y < 0 or y >= n or grid[x][y] == 'B':
            return -1  # Si estamos fuera del rango o en una bomba, no es válido
        if t == 2 * n - 1:
            return 0  # Casos base: hemos llegado al límite de pasos
        if (x, y, t) in dp:
            return dp[(x, y, t)]  # Devuelve el valor memoizado

        # Evaluamos las cuatro posibles direcciones
        max_capsulas = max(f(x + 1, y, t + 1), f(x - 1, y, t + 1),
                           f(x, y + 1, t + 1), f(x, y - 1, t + 1))

        # Si hay una cápsula en esta celda, sumamos 1
        if grid[x][y] == 'R':
            max_capsulas += 1

        dp[(x, y, t)] = max_capsulas
        return max_capsulas

    return f(0, 0, 0)
