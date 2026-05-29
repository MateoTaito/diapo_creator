import re

with open('slides.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Reemplazo del Código del Paso 3
old_step_3_code = """```python {all|1-3|4-7|8-11|12-15|16-19|20-21|1-21}
for fila in range(filas):
    for columna in range(columnas):
        if bosque[fila][columna] == 2:  # Árbol en llamas
            # Vecino arriba
            if fila - 1 >= 0 and bosque[fila - 1][columna] == 1:
                bosque[fila - 1][columna] = 3  # Estado intermedio
            # Vecino abajo
            if fila + 1 < filas and bosque[fila + 1][columna] == 1:
                bosque[fila + 1][columna] = 3
            # Vecino izquierda
            if columna - 1 >= 0 and bosque[fila][columna - 1] == 1:
                bosque[fila][columna - 1] = 3
            # Vecino derecha
            if columna + 1 < columnas and bosque[fila][columna + 1] == 1:
                bosque[fila][columna + 1] = 3
            # El árbol en llamas se consume
            bosque[fila][columna] = 0
            seguir_simulacion = 0  # Se quemó algo
```"""

new_step_3_code = """```python {all|1-3|4-5|6-7|8-9|10-11|12-14|1-14}
for fila in range(filas):
    for columna in range(columnas):
        if bosque[fila][columna] == 1:  # Árbol sano
            if fila - 1 >= 0 and (bosque[fila - 1][columna] == 2 or bosque[fila - 1][columna] == 4):
                bosque[fila][columna] = 3  # Estado intermedio
            if fila + 1 < filas and (bosque[fila + 1][columna] == 2 or bosque[fila + 1][columna] == 4):
                bosque[fila][columna] = 3
            if columna - 1 >= 0 and (bosque[fila][columna - 1] == 2 or bosque[fila][columna - 1] == 4):
                bosque[fila][columna] = 3
            if columna + 1 < columnas and (bosque[fila][columna + 1] == 2 or bosque[fila][columna + 1] == 4):
                bosque[fila][columna] = 3
        elif bosque[fila][columna] == 2: # Árbol en llamas
            bosque[fila][columna] = 4  # Árbol consumiéndose
            seguir_simulacion = 0
```"""
content = content.replace(old_step_3_code, new_step_3_code)

# 2. Reemplazo de la explicación del Paso 3
old_step_3_exp = """- <span class="highlight-blue">Línea 1-3:</span> Recorremos toda la matriz buscando árboles en llamas (`2`)
- <span class="highlight-orange">Estado intermedio `3`:</span> Marcamos los árboles que se quemarán en esta iteración
  - Esto evita que un árbol queme a sus vecinos <strong>instantáneamente</strong> en la misma iteración
- <span class="highlight-blue">Línea 5, 9, 12, 15:</span> Cada vecino verifica que esté dentro de los límites
  - `fila - 1 >= 0` → existe fila superior
  - `fila + 1 < filas` → existe fila inferior
  - `columna - 1 >= 0` → existe columna izquierda
  - `columna + 1 < columnas` → existe columna derecha
- <span class="highlight-magenta">Línea 18:</span> El árbol en llamas se convierte en tierra vacía (`0`)
- <span class="highlight-magenta">Línea 19:</span> Flag para continuar la simulación"""

new_step_3_exp = """- <span class="highlight-blue">Lógica Inversa:</span> En lugar de buscar el fuego, buscamos árboles sanos (`1`) y revisamos si el fuego (vecinos `2` o `4`) los alcanza.
- <span class="highlight-orange">Estados `3` y `4`:</span> `3` es un árbol sano que arderá pronto. `4` es un árbol en llamas a punto de consumirse.
- <span class="highlight-blue">Línea 4-11:</span> Cada vecino verifica que esté dentro de los límites y ardiendo (`2` o `4`).
- <span class="highlight-magenta">Línea 12-14:</span> El árbol en llamas cambia al estado transitorio `4` y se activa el flag de simulación."""
content = content.replace(old_step_3_exp, new_step_3_exp)

# 3. Reemplazo del código de Conversión
old_step_3_conv = """```python {all|1-4|5-7|1-7}
for fila in range(filas):
    for columna in range(columnas):
        if bosque[fila][columna] == 3:
            bosque[fila][columna] = 2  # Ahora quema en la siguiente iteración
```"""

new_step_3_conv = """```python {all|1-3|4-5|6-7|1-7}
for fila in range(filas):
    for columna in range(columnas):
        if bosque[fila][columna] == 3:
            bosque[fila][columna] = 2  # Pasa a ser foco de incendio
        elif bosque[fila][columna] == 4:
            bosque[fila][columna] = 0  # Pasa a ser tierra vacía
```"""
content = content.replace(old_step_3_conv, new_step_3_conv)

# 4. Reemplazo explicación de Conversión
old_step_3_conv_exp = """- Después de quemar todos los vecinos, convertimos los `3` en `2`
- Los árboles que eran `3` ahora son <span class="highlight-orange">focos de incendio</span> para el <strong>siguiente turno</strong>
- Esto garantiza que la propagación sea <strong>paso a paso</strong>, no instantánea"""

new_step_3_conv_exp = """- Convertimos los árboles marcados con `3` (por quemarse) al estado `2` (en llamas)
- Convertimos los árboles marcados con `4` (consumiéndose) al estado `0` (tierra vacía)
- Usar `3` y `4` garantiza que la propagación y consumo ocurran <strong>paso a paso</strong>."""
content = content.replace(old_step_3_conv_exp, new_step_3_conv_exp)


# 5. Reemplazo Texto de Transición
old_step_4_text = """<span class="highlight-magenta">Problema:</span> Si quemamos directamente `1 → 2`, un árbol podría propagar fuego a todos sus vecinos en una sola iteración.

<span class="highlight-blue">Solución:</span> Usamos un estado intermedio `3`

```
Iteración actual:
  1 → 3 (se quemó, pero aún no quema)
  2 → 0 (se consumió)

Entre iteraciones:
  3 → 2 (ahora es foco de incendio)
```

<span class="highlight-orange">Flujo completo de estados:</span>

```
1 (sano) → 3 (quemándose) → 2 (en llamas) → 0 (cenizas)
```"""

new_step_4_text = """<span class="highlight-magenta">Problema:</span> Si cambiamos directamente `1 → 2` y `2 → 0`, alteramos la grilla asincrónicamente durante el análisis.

<span class="highlight-blue">Solución:</span> Usamos dos estados intermedios: `3` y `4`

```
Iteración actual (Análisis):
  1 → 3 (se quemará en el próximo turno)
  2 → 4 (se consumirá al final del turno)

Entre iteraciones (Aplicación):
  3 → 2 (ahora es foco de incendio)
  4 → 0 (ahora es ceniza)
```

<span class="highlight-orange">Flujo completo de estados:</span>

```
1 (sano) → 3 (por quemarse) → 2 (en llamas) → 4 (consumiéndose) → 0 (cenizas)
```"""
content = content.replace(old_step_4_text, new_step_4_text)

# 6. Reemplazo Código de Transición
old_step_4_code = """```python {all|1-2|3-17|18-21|1-21}
seguir_simulacion = 1  # Asumo que no se quemará nada

for fila in range(filas):
    for columna in range(columnas):
        if bosque[fila][columna] == 2:
            if fila - 1 >= 0 and bosque[fila - 1][columna] == 1:
                bosque[fila - 1][columna] = 3
            if fila + 1 < filas and bosque[fila + 1][columna] == 1:
                bosque[fila + 1][columna] = 3
            if columna - 1 >= 0 and bosque[fila][columna - 1] == 1:
                bosque[fila][columna - 1] = 3
            if columna + 1 < columnas and bosque[fila][columna + 1] == 1:
                bosque[fila][columna + 1] = 3
            bosque[fila][columna] = 0
            seguir_simulacion = 0

for fila in range(filas):
    for columna in range(columnas):
        if bosque[fila][columna] == 3:
            bosque[fila][columna] = 2
```"""

new_step_4_code = """```python {all|1-2|3-15|16-21|1-21}
seguir_simulacion = 1  # Asumo que no se quemará nada

for fila in range(filas):
    for columna in range(columnas):
        if bosque[fila][columna] == 1:
            if fila - 1 >= 0 and (bosque[fila - 1][columna] == 2 or bosque[fila - 1][columna] == 4):
                bosque[fila][columna] = 3
            if fila + 1 < filas and (bosque[fila + 1][columna] == 2 or bosque[fila + 1][columna] == 4):
                bosque[fila][columna] = 3
            if columna - 1 >= 0 and (bosque[fila][columna - 1] == 2 or bosque[fila][columna - 1] == 4):
                bosque[fila][columna] = 3
            if columna + 1 < columnas and (bosque[fila][columna + 1] == 2 or bosque[fila][columna + 1] == 4):
                bosque[fila][columna] = 3
        elif bosque[fila][columna] == 2:
            bosque[fila][columna] = 4
            seguir_simulacion = 0

for fila in range(filas):
    for columna in range(columnas):
        if bosque[fila][columna] == 3:
            bosque[fila][columna] = 2
        elif bosque[fila][columna] == 4:
            bosque[fila][columna] = 0
```"""
content = content.replace(old_step_4_code, new_step_4_code)

# 7. Reemplazo del Flujo de Ciclo
old_step_5_list = """1. <span class="highlight-blue">Asumir que no se quemará nada</span> → `seguir_simulacion = 1`
2. <span class="highlight-blue">Recorrer el bosque</span> buscando árboles en llamas
3. <span class="highlight-orange">Quemar vecinos</span> marcándolos como `3`
4. <span class="highlight-magenta">Consumir árboles en llamas</span> → `2 → 0`
5. <span class="highlight-magenta">Convertir estados intermedios</span> → `3 → 2`
6. <span class="highlight-blue">Imprimir el estado actual</span> del bosque
7. <span class="highlight-blue">Incrementar contador</span> de iteraciones
8. <span class="highlight-orange">Verificar flag:</span> Si `seguir_simulacion == 0`, repetir"""

new_step_5_list = """1. <span class="highlight-blue">Asumir que simulación finaliza</span> → `seguir_simulacion = 1`
2. <span class="highlight-blue">Buscar árboles sanos (`1`) y en llamas (`2`)</span>
3. <span class="highlight-orange">Marcar amenazas a vecinos sanos</span> → `1 → 3`
4. <span class="highlight-magenta">Marcar consumo de llamas</span> → `2 → 4`, `seguir_simulacion = 0`
5. <span class="highlight-magenta">Resolver estados</span> → `3 → 2` y `4 → 0`
6. <span class="highlight-blue">Imprimir el estado actual</span> del bosque
7. <span class="highlight-blue">Incrementar contador</span> de iteraciones
8. <span class="highlight-orange">Verificar flag:</span> Si `seguir_simulacion == 0`, repetir"""
content = content.replace(old_step_5_list, new_step_5_list)


# 8. Reemplazo Código Final del Ciclo
old_step_5_code = """```python {all|1-3|4|5-20|21-30|31|1-31}
seguir_simulacion = 0
numero_iteracion = 0
while seguir_simulacion == 0:
    seguir_simulacion = 1
    
    for fila in range(filas):
        for columna in range(columnas):
            if bosque[fila][columna] == 2:
                if fila - 1 >= 0 and bosque[fila - 1][columna] == 1:
                    bosque[fila - 1][columna] = 3
                if fila + 1 < filas and bosque[fila + 1][columna] == 1:
                    bosque[fila + 1][columna] = 3
                if columna - 1 >= 0 and bosque[fila][columna - 1] == 1:
                    bosque[fila][columna - 1] = 3
                if columna + 1 < columnas and bosque[fila][columna + 1] == 1:
                    bosque[fila][columna + 1] = 3
                bosque[fila][columna] = 0
                seguir_simulacion = 0
    
    for fila in range(filas):
        for columna in range(columnas):
            if bosque[fila][columna] == 3:
                bosque[fila][columna] = 2
    
    print(f"Iteración: {numero_iteracion}")
    
    # Imprimir bosque_visual...
    
    numero_iteracion += 1
```"""

new_step_5_code = """```python {all|1-3|4|5-18|19-25|26|1-26}
seguir_simulacion = 0
numero_iteracion = 0
while seguir_simulacion == 0:
    seguir_simulacion = 1
    
    for fila in range(filas):
        for columna in range(columnas):
            if bosque[fila][columna] == 1:
                if fila - 1 >= 0 and (bosque[fila - 1][columna] == 2 or bosque[fila - 1][columna] == 4):
                    bosque[fila][columna] = 3
                if fila + 1 < filas and (bosque[fila + 1][columna] == 2 or bosque[fila + 1][columna] == 4):
                    bosque[fila][columna] = 3
                if columna - 1 >= 0 and (bosque[fila][columna - 1] == 2 or bosque[fila][columna - 1] == 4):
                    bosque[fila][columna] = 3
                if columna + 1 < columnas and (bosque[fila][columna + 1] == 2 or bosque[fila][columna + 1] == 4):
                    bosque[fila][columna] = 3
            elif bosque[fila][columna] == 2:
                bosque[fila][columna] = 4
                seguir_simulacion = 0
    
    for fila in range(filas):
        for columna in range(columnas):
            if bosque[fila][columna] == 3:
                bosque[fila][columna] = 2
            elif bosque[fila][columna] == 4:
                bosque[fila][columna] = 0
    
    print(f"Iteración: {numero_iteracion + 1}")
    
    # Imprimir bosque_visual...
    
    numero_iteracion += 1
```"""
content = content.replace(old_step_5_code, new_step_5_code)

with open('slides_alt.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("¡Diapositivas alternativas generadas exitosamente!")
