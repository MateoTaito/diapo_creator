matriz0 = []
matriz1 = []
for i in range(3):
    matriz0.append([])
    matriz1.append([])
    for j in range(3):
        num1 = int(
            input(f"Introduce el número para la posición ({i}, {j}) de la matriz 0: ")
        )
        num2 = int(
            input(f"Introduce el número para la posición ({i}, {j}) de la matriz 1: ")
        )
        matriz0[i].append(num1)
        matriz1[i].append(num2)

print("Matriz 0:")
for fila in matriz0:
    print(fila)

print("Matriz 1:")
for fila in matriz1:
    print(fila)
