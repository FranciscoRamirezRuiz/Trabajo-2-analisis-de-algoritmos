# main.py

from grid import inicializar_grid
from dp_solver import escape_tridimensional, escape_hash
from utils import medir_tiempo
from memory_profiler import memory_usage
import matplotlib.pyplot as plt

def medir_memoria(func, *args):
    """
    Mide el uso de memoria de una función.

    Args:
    func (function): La función a medir.
    *args: Argumentos a pasar a la función.

    Returns:
    tuple: Resultado de la función y el uso máximo de memoria (en MiB).
    """
    mem_usage = memory_usage((func, args))
    return mem_usage[-1]  # Memoria máxima utilizada

def realizar_pruebas():
    tamaños = [10, 20, 30, 40]
    tiempos_tridimensional = []
    tiempos_hash = []
    memoria_tridimensional = []
    memoria_hash = []

    print(f"{'Tamaño':<10} {'Tiempo Tridimensional (s)':<25} {'Memoria Tridimensional (MiB)':<30} "
          f"{'Tiempo Hash (s)':<20} {'Memoria Hash (MiB)'}")
    print("-" * 95)

    for n in tamaños:
        # Generar la cuadrícula aleatoria
        grid = inicializar_grid(n)

        # Medir el tiempo de ejecución y uso de memoria para la versión tridimensional
        print(f"Probando tamaño: {n}x{n}")
        
        tiempo_tridimensional, _ = medir_tiempo(escape_tridimensional, grid, n)
        memoria_tridimensional.append(medir_memoria(escape_tridimensional, grid, n))
        tiempos_tridimensional.append(tiempo_tridimensional)

        # Medir el tiempo de ejecución y uso de memoria para la versión con hash
        tiempo_hash, _ = medir_tiempo(escape_hash, grid, n)
        memoria_hash.append(medir_memoria(escape_hash, grid, n))
        tiempos_hash.append(tiempo_hash)

        # Imprimir resultados por cada tamaño
        print(f"{n:<10} {tiempo_tridimensional:<25.6f} {memoria_tridimensional[-1]:<30.6f} "
              f"{tiempo_hash:<20.6f} {memoria_hash[-1]:.6f}")

    # Graficar los resultados
    fig, ax1 = plt.subplots()

    # Gráfico de tiempos de ejecución
    ax1.set_xlabel('Tamaño de la cuadrícula (n)')
    ax1.set_ylabel('Tiempo de ejecución (segundos)', color='tab:blue')
    ax1.plot(tamaños, tiempos_tridimensional, color='tab:blue', label='Tridimensional')
    ax1.plot(tamaños, tiempos_hash, color='tab:orange', label='Hash')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    # Crear un segundo eje para el uso de memoria
    ax2 = ax1.twinx()
    ax2.set_ylabel('Uso de memoria (MiB)', color='tab:red')
    ax2.plot(tamaños, memoria_tridimensional, color='tab:red', linestyle='--', label='Memoria Tridimensional')
    ax2.plot(tamaños, memoria_hash, color='tab:green', linestyle='--', label='Memoria Hash')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    # Títulos y leyenda
    plt.title('Comparación entre las Estrategias de Memorización')
    fig.tight_layout()  # Ajustar para que no se sobrepongan los ejes
    plt.legend(loc='upper left')
    plt.show()

def main():
    realizar_pruebas()

if __name__ == "__main__":
    main()
