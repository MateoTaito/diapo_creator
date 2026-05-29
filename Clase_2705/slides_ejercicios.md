---
theme: default
title: "Ejercicios Prácticos: Listas y Ciclos"
class: text-left
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Ejercicios Prácticos: Listas y Ciclos

## Ejercicios de Aplicación en Python

### Clase de Programación

<div class="mt-6" style="color: #1a2744; font-weight: 600;">
Profesor: Mateo Taito Stambuk
</div>

<div class="mt-2 text-sm" style="color: #8b1a6e;">
Email: <a href="mailto:mateo.taitos@edu.uai.cl" style="color: #8b1a6e; border: none;">mateo.taitos@edu.uai.cl</a>
</div>

<div class="mt-4 text-sm" style="color: #c45200;">
27 de Mayo, 2026
</div>

<style>
.slidev-layout h1 {
  color: #1a2744;
}
.slidev-layout h2 {
  color: #2d3e5f;
}
.slidev-layout h3 {
  color: #8b1a6e;
}
strong {
  color: #1a2744;
}
a {
  color: #c45200;
  font-weight: 600;
  text-decoration: none;
  border-bottom: 2px solid #c45200;
  transition: all 0.2s;
}
a:hover {
  color: #8b1a6e;
  border-color: #8b1a6e;
}
</style>

---
layout: center
class: text-center
---

# Objetivos de la Clase

<div class="text-left mt-8 space-y-4">

- <span class="highlight-magenta">Repasar</span> el uso de índices para iterar sobre listas
- <span class="highlight-magenta">Relacionar</span> datos almacenados en listas paralelas (unidimensionales)
- <span class="highlight-magenta">Aplicar</span> ciclos anidados para problemas simples en 2D
- <span class="highlight-magenta">Desarrollar</span> lógica para imprimir figuras en pantalla (patrones)

</div>

<style>
.highlight-magenta {
  color: #8b1a6e;
  font-weight: 700;
}
.highlight-orange {
  color: #c45200;
  font-weight: 700;
}
.highlight-blue {
  color: #1a2744;
  font-weight: 700;
}
</style>

---
layout: section
---

<div class="section-divider section-blue">
<span class="section-number">1</span>
<h2>Listas Paralelas por Índice</h2>
</div>

<style>
.section-divider {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  justify-content: center;
  padding: 3rem 0;
}
.section-number {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: #1a2744;
  color: white;
  font-size: 2.5rem;
  font-weight: 800;
}
.section-divider h2 {
  color: #1a2744;
  font-size: 2.5rem;
  margin: 0;
}
.section-blue .section-number {
  background: #1a2744;
}
.section-blue h2 {
  color: #1a2744;
}
</style>

---

# Ejercicio 1: El Mejor Promedio

## Enunciado del Problema

Tenemos dos listas con información sobre estudiantes:
1. Una lista con los **nombres** de los alumnos.
2. Una lista con sus **calificaciones finales** (en el mismo orden).

<span class="highlight-magenta">Misión:</span> 
1. Encontrar el alumno con la **mejor calificación**.
2. Mostrar su nombre y su nota en pantalla.

<v-clicks>

- **Restricción:** No se pueden usar funciones avanzadas como `zip()` o `.index()`.
- Debemos recorrer las listas usando sus **índices**.

</v-clicks>

---

# Ejercicio 1: Planteamiento

Tenemos las siguientes listas iniciales:

```python
nombres = ["Ana", "Juan", "Pedro", "Sofía", "Luis"]
notas = [4.5, 6.2, 5.8, 6.9, 5.0]
```

**La relación por índice:**

- El índice `0` corresponde a Ana (nota 4.5).
- El índice `1` corresponde a Juan (nota 6.2).
- Y así sucesivamente...

<v-clicks>

<span class="highlight-orange">Estrategia:</span>
- Definir variables para guardar la `nota_maxima` y el `mejor_alumno`.
- Usar un `for` iterando desde `0` hasta el largo de la lista.
- Comparar cada nota y actualizar si encontramos una mayor.

</v-clicks>

---

# Ejercicio 1: Código Paso a Paso

```python {all|1-5|7-13|14-15|1-15}
# 1. Definimos las listas
nombres = ["Ana", "Juan", "Pedro", "Sofía", "Luis"]
notas = [4.5, 6.2, 5.8, 6.9, 5.0]

cantidad_alumnos = len(nombres)

# 2. Inicializamos variables (buscando un máximo)
mejor_nota = -1.0
mejor_alumno = ""

# 3. Recorremos usando índice
for i in range(cantidad_alumnos):
    if notas[i] > mejor_nota:
        mejor_nota = notas[i]
        mejor_alumno = nombres[i]

# 4. Resultado
print(f"El mejor alumno es {mejor_alumno} con un {mejor_nota}")
```

---

# Ejercicio 1: Explicación Detallada

<v-clicks>

- <span class="highlight-blue">Línea 5:</span> Usamos `len(nombres)` para saber cuántos elementos hay. Sirve para ambas porque miden lo mismo.
- <span class="highlight-orange">Líneas 8-9:</span> Iniciamos `mejor_nota` en `-1.0`. Así nos aseguramos de que el primer valor real siempre será mayor.
- <span class="highlight-magenta">Línea 12:</span> `range(cantidad_alumnos)` genera la secuencia `0, 1, 2, 3, 4`.
- <span class="highlight-blue">Líneas 13-15:</span> Comparamos y, si la nota actual es mayor, sobrescribimos nuestros registros.
- **¡El truco está en usar el mismo índice (`i`) para acceder a la nota (`notas[i]`) y al nombre correspondiente (`nombres[i]`).**

</v-clicks>

---
layout: section
---

<div class="section-divider section-magenta">
<span class="section-number">2</span>
<h2>Impresión de Figuras</h2>
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

# Ejercicio 2: Triángulo Rectángulo Invertido

## Enunciado del Problema

Se pide crear un programa que dibuje un triángulo rectángulo en la pantalla utilizando el carácter asterisco (`*`). 

El usuario define (o dejamos en código duro) la **altura**. 
Si la altura es `5`, se debe ver así:

```text
* * * * *
* * * *
* * *
* *
*
```

---

# Ejercicio 2: Planteamiento

Para dibujar en consola, imprimimos línea por línea (de arriba hacia abajo).

- **Fila 1:** 5 asteriscos
- **Fila 2:** 4 asteriscos
- **Fila i:** `altura - i + 1` asteriscos (o iteramos en reversa)

<v-clicks>

<span class="highlight-orange">Dos enfoques posibles:</span>

1. **Uso de ciclos anidados:** Un ciclo para las filas y otro interno para los asteriscos (enfoque universal).
2. **Multiplicación de strings:** Multiplicar `*` por el número de la fila (atajo de Python).

</v-clicks>

---

# Ejercicio 2: Código con Ciclos Anidados

Este es el enfoque clásico, que te servirá si en el futuro programas en C, Java o C#.

```python {all|1-2|4|5-6|7|1-7}
altura = 5
print("Método 1: Ciclos Anidados")

for fila in range(altura, 0, -1):
    for columna in range(fila):
        print("* ", end="") # end="" evita el salto de línea
    print() # Salto de línea al terminar la fila
```

<v-clicks>

- <span class="highlight-blue">Línea 4:</span> `range(altura, 0, -1)` itera en reversa desde `5` hasta `1`.
- <span class="highlight-orange">Línea 5:</span> El ciclo interno depende de la `fila` actual. En la primera iteración, al valer `5`, este ciclo se ejecuta 5 veces.
- <span class="highlight-magenta">Línea 7:</span> El `print()` vacío genera el enter/salto a la siguiente línea del terminal una vez que terminamos de dibujar esa fila.

</v-clicks>

---

# Ejercicio 2: El atajo de Python

En Python, podemos simplificar el proceso porque los "strings" se pueden multiplicar por un entero.

```python {all|1-2|4-5|1-5}
altura = 5
print("Método 2: Multiplicación de Strings")

for fila in range(altura, 0, -1):
    print("* " * fila)
```

<v-clicks>

- <span class="highlight-blue">La magia de `"* " * 3`</span> dará como resultado la cadena combinada `"* * * "`.
- Esto nos permite evitar el segundo ciclo (`for` interno), haciendo el código mucho más simple.
- **Dato:** Es importante conocer ambos. Las lógicas de multiplicar strings no siempre existen en otros lenguajes.

</v-clicks>

---
layout: center
class: text-center
---

# ¡Gracias!

<div class="mt-8 text-xl" style="color: #1a2744;">
¿Preguntas sobre estos ejercicios?
</div>
