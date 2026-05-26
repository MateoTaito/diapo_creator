import random

filas = 10
columnas = 20
bosque = []

# Inicializo el bosque con 1 (árbol sano) y 2 (árbol en llamas). La probabilidad de incendio inicial es del 10%.
for fila in range(filas):
    bosque.append([])
    for columna in range(columnas):
        if random.randint(0, 10) <= 9:
            bosque[fila].append(1)
        else:
            bosque[fila].append(2)

bosque_visual = []
for fila in range(filas):
    bosque_visual.append([])
    for columna in range(columnas):
        if bosque[fila][columna] == 0:
            bosque_visual[fila].append(".")
        elif bosque[fila][columna] == 1:
            bosque_visual[fila].append("T")
        elif bosque[fila][columna] == 2:
            bosque_visual[fila].append("X")

for fila in range(filas):
    for columna in range(columnas):
        print(bosque_visual[fila][columna], end=" ")
    print()

# Lógica de quemado
seguir_simulacion = 0  # Flag para saber si se quemó algo en la iteración, si no se quemó nada, se detiene el proceso
numero_iteracion = 0  # Contador de iteraciones, para saber cuántas iteraciones se necesitan para quemar todo el mapa
while seguir_simulacion == 0:  # Cuando no se quema nada, se detiene el proceso
    seguir_simulacion = 1  # Asumo que no se quemará nada, si se quema algo, se cambia a 0

    # Lógica para quemar los árboles, si hay un árbol encendido, se quema al rededor, y el árbol se apaga. El proceso se repite hasta que no se queme nada.
    for fila in range(filas):
        for columna in range(columnas):
            if bosque[fila][columna] == 2:  # Si hay un arbol encendido, se quema al rededor
                if (
                    fila - 1 >= 0 and bosque[fila - 1][columna] == 1
                ):  # Si el árbol de arriba existe, se quema
                    bosque[fila - 1][columna] = (
                        3  # OJO: el 3 es un estado intermedio para marcar que ese árbol se quemó en esta iteración y se hace para que no quemen instantaneamente a los demás
                    )
                if (
                    fila + 1 < filas and bosque[fila + 1][columna] == 1
                ):  # Si el árbol de abajo existe, se quema
                    bosque[fila + 1][columna] = 3
                if (
                    columna - 1 >= 0 and bosque[fila][columna - 1] == 1
                ):  # Si el árbol de la izquierda existe, se quema
                    bosque[fila][columna - 1] = 3
                if (
                    columna + 1 < columnas and bosque[fila][columna + 1] == 1
                ):  # Si el árbol de la derecha existe, se quema
                    bosque[fila][columna + 1] = 3
                bosque[fila][columna] = 0
                seguir_simulacion = 0  # Si se quemó algo, cambio el flag a 0 para que el proceso continúe

    # Lógica para convertir los arboles que se quemaron en esta iteración en árboles que ahora queman al resto
    for fila in range(filas):
        for columna in range(columnas):
            if (
                bosque[fila][columna] == 3
            ):  # Si hay un árbol que se quemó en esta iteración, pasa a ser foco de incendio para la siguiente iteración
                bosque[fila][columna] = 2

    print("Iteración terminada")
    print(f"Número de iteraciones: {numero_iteracion}")

    # Imprimo el mapa después de cada iteración
    bosque_visual = []
    for fila in range(filas):
        bosque_visual.append([])
        for columna in range(columnas):
            if bosque[fila][columna] == 0:
                bosque_visual[fila].append(".")
            elif bosque[fila][columna] == 1:
                bosque_visual[fila].append("T")
            elif bosque[fila][columna] == 2:
                bosque_visual[fila].append("X")

    for fila in range(filas):
        for columna in range(columnas):
            print(bosque_visual[fila][columna], end=" ")
        print()
    numero_iteracion += 1
