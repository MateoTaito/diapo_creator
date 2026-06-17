# Ejercicio 3: Funcion encontrar_mayor(numeros) con entradas y salida
# Recibe una lista y devuelve el numero mayor con return

# 1. Definicion de la funcion
def encontrar_mayor(numeros):
    mayor = numeros[0]
    for i in range(1, len(numeros)):
        if numeros[i] > mayor:
            mayor = numeros[i]
    return mayor

# 2. Programa principal
lista_a = [4, 2, 8, 1, 9, 5, 3]
lista_b = [10, 5, 7]
lista_c = [-3, -10, -1, -5]

print(f"Mayor de A: {encontrar_mayor(lista_a)}")
print(f"Mayor de B: {encontrar_mayor(lista_b)}")
print(f"Mayor de C: {encontrar_mayor(lista_c)}")
