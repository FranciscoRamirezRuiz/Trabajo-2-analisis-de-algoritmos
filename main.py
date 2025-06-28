# main.py

from generar_mapa import generar_mapa
from solucion_pd import escape_tridimensional, escape_hash
from utilidades import medir_tiempo
from memory_profiler import memory_usage
import matplotlib.pyplot as plt

def medir_memoria(funcion, *args):
    """
    Mide el uso de memoria máximo de una función.
    """
    uso_memoria = memory_usage((funcion, args))
    return uso_memoria[-1]

def pruebas_comparativas():
    tamanos = [10, 20, 30, 40]
    tiempos_tridimensional = []
    tiempos_hash = []
    memoria_tridimensional = []
    memoria_hash = []

    print(f"{'Tamaño':<10} {'Tiempo Tridimensional (s)':<25} {'Memoria Tridimensional (MiB)':<30} "
          f"{'Tiempo Hash (s)':<25} {'Memoria Hash (MiB)'}")
    print("-" * 105)

    for n in tamanos:
        mapa = generar_mapa(n)

        # Tridimensional
        tiempo_tri, _ = medir_tiempo(escape_tridimensional, mapa, n)
        mem_tri = medir_memoria(escape_tridimensional, mapa, n)
        tiempos_tridimensional.append(tiempo_tri)
        memoria_tridimensional.append(mem_tri)

        # Hash
        tiempo_hash, _ = medir_tiempo(escape_hash, mapa, n)
        mem_hash = medir_memoria(escape_hash, mapa, n)
        tiempos_hash.append(tiempo_hash)
        memoria_hash.append(mem_hash)

        print(f"{n:<10} {tiempo_tri:<25.6f} {mem_tri:<30.6f} {tiempo_hash:<25.6f} {mem_hash:.6f}")

    # Gráfico
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Tamaño de la cuadrícula (n)')
    ax1.set_ylabel('Tiempo de ejecución (s)', color='tab:blue')
    ax1.plot(tamanos, tiempos_tridimensional, color='tab:blue', label='Tridimensional')
    ax1.plot(tamanos, tiempos_hash, color='tab:orange', label='Hash')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Uso de memoria (MiB)', color='tab:red')
    ax2.plot(tamanos, memoria_tridimensional, color='tab:red', linestyle='--', label='Memoria Tridimensional')
    ax2.plot(tamanos, memoria_hash, color='tab:green', linestyle='--', label='Memoria Hash')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    plt.title('Comparación de Estrategias de Memorización')
    fig.tight_layout()
    plt.legend(loc='upper left')
    plt.show()

def main():
    pruebas_comparativas()

if __name__ == "__main__":
    main()
