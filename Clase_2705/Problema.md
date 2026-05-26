## Problema: Simulación de Propagación de Incendio

El objetivo es modelar cómo se propaga un incendio en un bosque a lo largo del tiempo. El bosque se representa mediante una matriz (una lista de listas) de tamaño $N \times M$.

Cada celda de la matriz representa una parcela de tierra y puede tener uno de tres estados:

* `0`: Tierra vacía o cenizas.
* `1`: Árbol sano.
* `2`: Árbol en llamas.

### Reglas de propagación (Transición de estados)

En cada turno (o iteración de tiempo), el estado del bosque cambia simultáneamente según las siguientes reglas:

1. Un **árbol sano (`1`)** se incendia y pasa a ser un **árbol en llamas (`2`)** si al menos uno de sus vecinos adyacentes (arriba, abajo, izquierda o derecha) está actualmente en llamas.
2. Un **árbol en llamas (`2`)** se consume completamente y pasa a ser **tierra vacía (`0`)** en el siguiente turno.
3. La **tierra vacía (`0`)** permanece como tierra vacía.

---

### Desglose paso a paso (Tiempo estimado: 1 hora)

Para resolver este problema de manera ordenada, el desarrollo debe dividirse en los siguientes hitos:

#### Paso 1: Inicialización del Bosque (10 minutos)

Crea una función que reciba las dimensiones $N$ (filas) y $M$ (columnas) y devuelva una lista anidada llena de árboles sanos (`1`), excepto por unas pocas celdas específicas que serán los focos iniciales del incendio (`2`).

* *Requisito:* Utilizar ciclos anidados o comprensión de listas para generar la estructura.

#### Paso 2: Visualización de la Matriz (10 minutos)

Escribe una función que reciba la matriz y la imprima en la consola de forma legible.

* *Requisito:* Recorrer la lista anidada con un ciclo `for` dentro de otro `for`. Para hacerlo más visual, puedes hacer que imprima caracteres como `. ` (vacío), `T ` (árbol), y `X ` (fuego).

#### Paso 3: Análisis de Vecindario (20 minutos)

Este es el núcleo lógico del problema. Desarrolla una función que reciba la matriz y unas coordenadas específicas `(fila, columna)`. La función debe revisar los vecinos adyacentes (ortogonales) de esa celda y determinar si hay fuego cerca.

* *Reto principal:* Manejar los bordes de la matriz. Si estás analizando la celda `(0,0)`, no puedes buscar un vecino en la fila `-1` porque dará un error de índice (o leerá el final de la lista de forma incorrecta). Deberás usar condiciones para no salirte de los límites de la lista anidada.

#### Paso 4: Generación del Nuevo Estado (10 minutos)

Crea una ciclo que genere el estado del **siguiente turno**.

#### Paso 5: El Ciclo de Simulación (10 minutos)

Finalmente, arma el programa principal. Solicita al usuario el número de turnos que desea simular. Utiliza un ciclo `while` o `for` para ejecutar la simulación paso a paso:

1. Imprime el estado actual del bosque.
2. Calcula el nuevo estado.
3. Actualiza la variable del bosque con el nuevo estado.
4. Repite hasta que se acaben los turnos o ya no queden árboles en llamas.

---

**Nota de implementación:** Este ejercicio fuerza la práctica intensiva de índices (`matriz[i][j]`), la comprensión de la mutabilidad de las listas en memoria y la abstracción de lógicas complejas en funciones más pequeñas y manejables.
