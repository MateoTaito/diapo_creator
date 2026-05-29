
- La mayoría de las celdas son <span class="highlight-blue">árboles sanos</span> (`1`)
- Algunas celdas son <span class="highlight-orange">focos iniciales de incendio</span> (`2`)

**Enfoque del código:**

- Probabilidad del 90% → árbol sano
- Probabilidad del 10% → árbol en llamas

```python
import random

filas = 10
columnas = 20
bosque = []
```

---

# Paso 1: Código de Inicialización

```python {all|1-2|3-6|1-6}
for fila in range(filas):
    bosque.append([])
    for columna in range(columnas):
        if random.randint(0, 10) <= 9:
            bosque[fila].append(1)  # Árbol sano
        else:
            bosque[fila].append(2)  # Árbol en llamas
```

<v-clicks>

- <span class="highlight-blue">Línea 1-2:</span> Iteramos por cada fila y creamos una lista vacía
- <span class="highlight-blue">Línea 3-6:</span> Para cada columna, decidimos el estado aleatoriamente
- `random.randint(0, 10)` genera un número entre 0 y 10
- Si es ≤ 9 (90%): <span class="highlight-blue">árbol sano</span> (`1`)
- Si es > 9 (10%): <span class="highlight-orange">árbol en llamas</span> (`2`)

</v-clicks>

---
layout: center
---

# Paso 1: Diagrama de Flujo

[Ver diagrama de inicialización](./diagramas/01-inicializacion.png)

---
layout: section
---

<div class="section-divider section-magenta">
<span class="section-number">2</span>
<h2>Visualización de la Matriz</h2>
</div>

<style>
.section-magenta .section-number {
  background: #8b1a6e;
}
.section-magenta h2 {
  color: #8b1a6e;
}
</style>

---

# Paso 2: Visualización

## Hacer el bosque legible para humanos

Convertimos los valores numéricos en caracteres visuales:

<div class="grid grid-cols-3 gap-4 mt-4">

<div class="state-card state-0">
<div class="state-value">.</div>
<div class="state-label">Tierra vacía</div>
</div>

<div class="state-card state-1">
<div class="state-value">T</div>
<div class="state-label">Árbol sano</div>
</div>

<div class="state-card state-2">
<div class="state-value">X</div>
<div class="state-label">Árbol en llamas</div>
</div>

</div>

**Requisito:** Recorrer la matriz con ciclos `for` anidados

---

# Paso 2: Código de Visualización

```python {all|1-3|4-7|8-10|1-10}
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
```

<v-clicks>

- <span class="highlight-blue">Línea 1-3:</span> Creamos una nueva matriz para los caracteres
- <span class="highlight-blue">Línea 4-10:</span> Recorremos cada celda y mapeamos el valor
- Usamos `if/elif` para seleccionar el carácter correcto

</v-clicks>

---

# Paso 2: Imprimir el Bosque

```python {all|1-4|5|1-5}
for fila in range(filas):
    for columna in range(columnas):
        print(bosque_visual[fila][columna], end=" ")
    print()
```

<v-clicks>

- <span class="highlight-blue">Línea 1-3:</span> Imprimimos cada carácter seguido de un espacio
- `end=" "` evita el salto de línea después de cada carácter
- <span class="highlight-blue">Línea 4:</span> `print()` sin argumentos genera el salto de línea al final de cada fila

**Resultado visual:**

```
T T T . X T T T T T
T T T T T T T X T T
. T T T T T T T T T
```

</v-clicks>

---
layout: center
---

# Paso 2: Diagrama de Flujo

[Ver diagrama de visualización](./diagramas/02-visualizacion.png)

---
layout: section
---

<div class="section-divider section-magenta">
<span class="section-number">3</span>
<h2>Análisis de Vecindario</h2>
</div>

---

# Paso 3: El Núcleo Lógico

## ¿Cómo saber si un árbol se incendia?

Para cada celda `(fila, columna)`, debemos revisar sus <span class="highlight-orange">vecinos ortogonales</span>:

```
        ↑ (fila-1, columna)
        |
← (fila, columna-1)  ●  → (fila, columna+1)
        |
        ↓ (fila+1, columna)
```

<span class="highlight-magenta">Reto principal:</span> Manejar los bordes de la matriz

- En `(0, 0)` no existe `fila - 1`
- En `(filas-1, columnas-1)` no existe `columna + 1`

---

# Paso 3: Lógica de Quemado

```python {all|1-3|4-7|8-11|12-15|16-19|20-21|1-21}
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
```

---

# Paso 3: Explicación Detallada

<v-clicks>

- <span class="highlight-blue">Línea 1-3:</span> Recorremos toda la matriz buscando árboles en llamas (`2`)
- <span class="highlight-orange">Estado intermedio `3`:</span> Marcamos los árboles que se quemarán en esta iteración
  - Esto evita que un árbol queme a sus vecinos <strong>instantáneamente</strong> en la misma iteración
- <span class="highlight-blue">Línea 5, 9, 12, 15:</span> Cada vecino verifica que esté dentro de los límites
  - `fila - 1 >= 0` → existe fila superior
  - `fila + 1 < filas` → existe fila inferior
  - `columna - 1 >= 0` → existe columna izquierda
  - `columna + 1 < columnas` → existe columna derecha
- <span class="highlight-magenta">Línea 18:</span> El árbol en llamas se convierte en tierra vacía (`0`)
- <span class="highlight-magenta">Línea 19:</span> Flag para continuar la simulación

</v-clicks>

---

# Paso 3: Manejo de Bordes

## ¿Por qué es importante?

```
Sin verificación de bordes:
bosque[-1][columna] → Lee la ÚLTIMA fila (¡error lógico!)
bosque[filas][columna] → IndexError (¡crash!)
```

**Solución aplicada:**

| Dirección | Condición | Significado |
|-----------|-----------|-------------|
| <span class="highlight-blue">Arriba</span> | `fila - 1 >= 0` | No estamos en la primera fila |
| <span class="highlight-blue">Abajo</span> | `fila + 1 < filas` | No estamos en la última fila |
| <span class="highlight-blue">Izquierda</span> | `columna - 1 >= 0` | No estamos en la primera columna |
| <span class="highlight-blue">Derecha</span> | `columna + 1 < columnas` | No estamos en la última columna |

---

# Paso 3: Conversión de Estado Intermedio

```python {all|1-4|5-7|1-7}
for fila in range(filas):
    for columna in range(columnas):
        if bosque[fila][columna] == 3:
            bosque[fila][columna] = 2  # Ahora quema en la siguiente iteración
```

<v-clicks>

- Después de quemar todos los vecinos, convertimos los `3` en `2`
- Los árboles que eran `3` ahora son <span class="highlight-orange">focos de incendio</span> para el <strong>siguiente turno</strong>
- Esto garantiza que la propagación sea <strong>paso a paso</strong>, no instantánea

</v-clicks>

---
layout: center
---

# Paso 3: Diagrama de Flujo

[Ver diagrama de vecindario](./diagramas/03-vecindario.png)

---
layout: section
---

<div class="section-divider section-orange">
<span class="section-number">4</span>
<h2>Generación del Nuevo Estado</h2>
</div>

<style>
.section-orange .section-number {
  background: #c45200;
}
.section-orange h2 {
  color: #c45200;
}
</style>

---

# Paso 4: Transición de Estados

## El estado intermedio `3` es clave

<span class="highlight-magenta">Problema:</span> Si quemamos directamente `1 → 2`, un árbol podría propagar fuego a todos sus vecinos en una sola iteración.

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
```

---

# Paso 4: Código Completo de Transición

```python {all|1-2|3-17|18-21|1-21}
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
```

---
layout: center
---

# Paso 4: Diagrama de Flujo

[Ver diagrama de nuevo estado](./diagramas/04-nuevo-estado.png)

---
layout: section
---

<div class="section-divider section-orange">
<span class="section-number">5</span>
<h2>El Ciclo de Simulación</h2>
</div>

---

# Paso 5: Programa Principal

## Estructura del ciclo principal

```python {all|1|2|3|4-6|7-10|1-10}
seguir_simulacion = 0
numero_iteracion = 0
while seguir_simulacion == 0:
    seguir_simulacion = 1
    
    # Lógica de quemado (Paso 3 y 4)
    # ...
    
    # Imprimir estado actual
    # ...
    
    numero_iteracion += 1
```

<v-clicks>

- <span class="highlight-magenta">Flag `seguir_simulacion`:</span> Controla cuándo detener la simulación
- <span class="highlight-blue">Contador `numero_iteracion`:</span> Registra cuántos turnos se ejecutaron
- <span class="highlight-orange">Condición del while:</span> Se detiene cuando no se quema nada más

</v-clicks>

---

# Paso 5: Flujo de Cada Iteración

En cada turno del ciclo `while`:

<v-clicks>

1. <span class="highlight-blue">Asumir que no se quemará nada</span> → `seguir_simulacion = 1`
2. <span class="highlight-blue">Recorrer el bosque</span> buscando árboles en llamas
3. <span class="highlight-orange">Quemar vecinos</span> marcándolos como `3`
4. <span class="highlight-magenta">Consumir árboles en llamas</span> → `2 → 0`
5. <span class="highlight-magenta">Convertir estados intermedios</span> → `3 → 2`
6. <span class="highlight-blue">Imprimir el estado actual</span> del bosque
7. <span class="highlight-blue">Incrementar contador</span> de iteraciones
8. <span class="highlight-orange">Verificar flag:</span> Si `seguir_simulacion == 0`, repetir

</v-clicks>

<strong>La simulación termina cuando:</strong>
- No quedan árboles en llamas
- O no hay árboles sanos adyacentes al fuego

---

# Paso 5: Código Completo del Ciclo

```python {all|1-3|4|5-20|21-30|31|1-31}
seguir_simulacion = 0
numero_iteracion = 0
while seguir_simulacion == 0:
    seguir_simulacion = 1
    
    for fila in range(filas):
        for columna in range(columnas):
            if bosque[fila][columna] == 2:
                if fila - 1 >= 0 and bosque[fila - 1][columna] == 1:
