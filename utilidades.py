# utilidades.py

import time

def medir_tiempo(funcion, *args):
    """
    Mide el tiempo de ejecución de una función.
    """
    inicio = time.time()
    resultado = funcion(*args)
    fin = time.time()
    return resultado, fin - inicio
