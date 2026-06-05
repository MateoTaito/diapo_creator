# Ejercicio 1: Analisis de Ventas Mensuales
# Listas paralelas (meses y ventas) con uso de .index()

# 1. Inicializacion: datos del problema
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
ventas = [120, 145, 160, 130, 175, 200, 210, 195, 180, 165, 150, 220]

# 2. Logica: calculos y busquedas
total = sum(ventas)
promedio = total / len(ventas)
max_ventas = max(ventas)
min_ventas = min(ventas)
pos_mejor = ventas.index(max_ventas)
pos_peor = ventas.index(min_ventas)

# 3. Salidas: mostrar los resultados
print(f"Total de ventas del anio: {total}")
print(f"Promedio mensual: {promedio:.2f} ventas")
print(f"Mejor mes: {meses[pos_mejor]} ({max_ventas} ventas)")
print(f"Peor mes: {meses[pos_peor]} ({min_ventas} ventas)")
