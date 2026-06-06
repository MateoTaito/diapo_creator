# Ejercicio 2: Marco Rectangular
# Impresion de un marco con asteriscos usando ciclos anidados

# 1. Inicializacion: dimensiones del marco
ancho = 5
alto = 10

# 2. Logica: recorrer filas y columnas
for fila in range(alto):
    for columna in range(ancho):
        es_borde = (
            (fila == 0)
            or (fila == alto - 1)
            or (columna == 0)
            or (columna == ancho - 1)
        )
        if es_borde:
            print("* ", end="")
        else:
            print("  ", end="")
    # 3. Salida: terminar la fila
    print()
