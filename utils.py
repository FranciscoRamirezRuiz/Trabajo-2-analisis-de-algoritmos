# utils.py

import time

def medir_tiempo(func, *args):
    """
    Mide el tiempo de ejecución de una función.
    
    Args:
    func (function): La función a medir.
    *args: Argumentos a pasar a la función.

    Returns:
    tuple: Resultado de la función y el tiempo de ejecución en segundos.
    """
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time
