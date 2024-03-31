"""
En este código, después de definir la base de conocimiento y la función de búsqueda de la mejor ruta, se solicita al usuario que ingrese la estación de origen y la estación de destino utilizando la función input(). Luego, se verifica si las estaciones ingresadas existen en la base de conocimiento antes de continuar con la búsqueda de la ruta óptima.

En este código:
 - base_conocimiento representa las conexiones entre las estaciones de transporte y los costos asociados a cada conexión.
 - La función encontrarRuta implementa el algoritmo de búsqueda de costo uniforme para encontrar la ruta óptima desde el origen hasta el destino.
 - Se utiliza una cola de prioridad (cola_prioridad) para mantener los nodos a explorar ordenados por el costo acumulado hasta el momento.
 - Se explora cada nodo en función de las conexiones definidas en la base de conocimiento hasta llegar al destino o hasta que no haya más nodos por explorar.
 - Finalmente, se imprime la ruta óptima encontrada. Si no se encuentra una ruta, se imprime un mensaje indicando que no se encontró ruta.
 - Puedes ajustar la base de conocimiento y los costos asociados según la red de transporte masivo real que estés modelando.
 
Para desarrollar un sistema inteligente que determine la mejor ruta para moverse desde un punto A hasta un punto B en un sistema de transporte masivo local utilizando reglas lógicas, podemos utilizar un enfoque basado en algoritmos de búsqueda. Aquí hay un ejemplo de cómo podrías implementarlo en Python utilizando el algoritmo de búsqueda de costo uniforme:

"""

import heapq  # Importa la librería heapq, que proporciona funciones para trabajar con colas de prioridad basadas en montículos

# Define la base de conocimiento que contiene las conexiones entre estaciones y los costos asociados
base_conocimiento = {
    "A": {"B": 5, "C": 7},
    "B": {"D": 4},
    "C": {"D": 6, "E": 8},
    "D": {"F": 3},
    "E": {"F": 7},
    "F": {"G": 2},
}

# Define la función encontrarRuta que encuentra la mejor ruta desde un origen hasta un destino
def encontrarRuta(origen, destino):
    cola_prioridad = [(0, origen, [])]  # Inicializa una cola de prioridad con el costo acumulado, el nodo actual y la ruta hasta el nodo actual
    visitados = set()  # Inicializa un conjunto para almacenar los nodos visitados durante la búsqueda

    while cola_prioridad:  # Bucle principal para buscar la mejor ruta
        costo_acumulado, nodo_actual, ruta_hasta_nodo_actual = heapq.heappop(cola_prioridad)  # Extrae el elemento con el menor costo acumulado de la cola de prioridad

        if nodo_actual == destino:  # Verifica si se ha llegado al destino
            return ruta_hasta_nodo_actual + [nodo_actual]  # Devuelve la ruta óptima encontrada hasta el momento

        if nodo_actual not in visitados:  # Verifica si el nodo actual no ha sido visitado aún
            visitados.add(nodo_actual)  # Agrega el nodo actual al conjunto de nodos visitados

            if nodo_actual in base_conocimiento:  # Verifica si el nodo actual tiene conexiones en la base de conocimiento
                for vecino, costo in base_conocimiento[nodo_actual].items():  # Itera sobre los vecinos del nodo actual y sus costos asociados
                    nueva_ruta = ruta_hasta_nodo_actual + [nodo_actual]  # Crea una nueva ruta que incluye el nodo actual
                    heapq.heappush(cola_prioridad, (costo_acumulado + costo, vecino, nueva_ruta))  # Agrega el vecino a la cola de prioridad con el nuevo costo acumulado

    return None  # Si no se encuentra ninguna ruta, devuelve None

# Imprime las rutas disponibles en el sistema mostrando todas las conexiones entre estaciones y sus costos asociados
print("Rutas disponibles en el sistema:")
for origen, destinos in base_conocimiento.items():
    print(f"Desde la estación {origen} se puede llegar a:")
    for destino, costo in destinos.items():
        print(f"- Estación {destino} con un costo de {costo}")

# Bucle principal para solicitar rutas múltiples al usuario
while True:
    origen = input("Ingrese la estación de origen (o 'exit' para salir): ").upper()  # Solicita la estación de origen al usuario
    if origen == 'EXIT':  # Verifica si el usuario quiere salir del programa
        break  # Sale del bucle principal si el usuario ingresa 'exit'
    
    destino = input("Ingrese la estación de destino: ").upper()  # Solicita la estación de destino al usuario

    # Verifica si las estaciones ingresadas existen en la base de conocimiento
    if origen not in base_conocimiento or destino not in base_conocimiento:
        print("Estación de origen o destino no válida.")  # Imprime un mensaje de error si alguna de las estaciones no es válida
    else:
        ruta_optima = encontrarRuta(origen, destino)  # Encuentra la mejor ruta desde el origen hasta el destino
        if ruta_optima:
            print(f"La mejor ruta desde {origen} hasta {destino} es: {' -> '.join(ruta_optima)}")  # Imprime la mejor ruta encontrada
        else:
            print(f"No se encontró ruta desde {origen} hasta {destino}")  # Imprime un mensaje si no se encuentra ninguna ruta
