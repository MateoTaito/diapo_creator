# Ejercicio 3: Promedio con Evaluaciones Variables
# Lista 2D irregular: cada estudiante tiene distinta cantidad de notas

# 1. Inicializacion: datos irregulares
nombres = ["Ana", "Juan", "Pedro", "Sofia", "Luis"]
notas = [
    [5.5, 6.0, 4.8],
    [6.2, 5.8, 6.5, 7.0, 5.5],
    [4.0, 5.5],
    [6.0, 5.5, 6.8, 6.2],
    [5.0]
]

promedios = []
suma_total = 0
cantidad_total = 0

# 2. Logica: recorrer listas irregulares
# OJO: len(notas[i]) es distinto para cada estudiante
for i in range(len(notas)):
    suma_est = 0
    for j in range(len(notas[i])):
        suma_est += notas[i][j]
    promedio = suma_est / len(notas[i])
    promedios.append(promedio)
    suma_total += suma_est
    cantidad_total += len(notas[i])

# 3. Salidas: mostrar resultados
for i in range(len(nombres)):
    print(f"{nombres[i]}: promedio {promedios[i]:.2f}")

pos_mejor = promedios.index(max(promedios))
print(f"Mejor estudiante: {nombres[pos_mejor]} con {promedios[pos_mejor]:.2f}")
print(f"Promedio del curso: {suma_total / cantidad_total:.2f}")
