# Ejemplo 2: Funcion calcular_promedio() con entradas y salida (return)
# Recibe una lista de notas y devuelve el promedio

# 1. Definicion de funciones
def calcular_promedio(notas):
    suma = 0
    for nota in notas:
        suma = suma + nota
    promedio = suma / len(notas)
    return promedio

# 2. Programa principal
notas_alumno = [5.5, 6.0, 4.8, 7.0, 5.2]
promedio_final = calcular_promedio(notas_alumno)
print(f"El promedio es: {promedio_final:.2f}")
