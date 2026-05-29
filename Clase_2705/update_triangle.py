import re

with open('slides_ejercicios.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Title
content = content.replace('# Ejercicio 2: Triángulo Rectángulo', '# Ejercicio 2: Triángulo Rectángulo Invertido')

# Replace Problem Statement Code Block
old_prob_code = """```text
*
* *
* * *
* * * *
* * * * *
```"""
new_prob_code = """```text
* * * * *
* * * *
* * *
* *
*
```"""
content = content.replace(old_prob_code, new_prob_code)

# Replace Planteamiento Explanation
old_plant = """- **Fila 1:** 1 asterisco
- **Fila 2:** 2 asteriscos
- **Fila i:** `i` asteriscos"""
new_plant = """- **Fila 1:** 5 asteriscos
- **Fila 2:** 4 asteriscos
- **Fila i:** `altura - i + 1` asteriscos (o iteramos en reversa)"""
content = content.replace(old_plant, new_plant)

# Replace Nested Loop Code Block
old_nested = """```python {all|1-2|4|5-6|7|1-7}
altura = 5
print("Método 1: Ciclos Anidados")

for fila in range(1, altura + 1):
    for columna in range(fila):
        print("* ", end="") # end="" evita el salto de línea
    print() # Salto de línea al terminar la fila
```"""
new_nested = """```python {all|1-2|4|5-6|7|1-7}
altura = 5
print("Método 1: Ciclos Anidados")

for fila in range(altura, 0, -1):
    for columna in range(fila):
        print("* ", end="") # end="" evita el salto de línea
    print() # Salto de línea al terminar la fila
```"""
content = content.replace(old_nested, new_nested)

# Replace Nested Loop Explanation
old_nested_exp = """- <span class="highlight-blue">Línea 4:</span> `range(1, altura + 1)` itera desde el `1` hasta el `5`.
- <span class="highlight-orange">Línea 5:</span> El ciclo interno depende de la `fila` actual. Si estamos en la fila `3`, este ciclo se ejecuta 3 veces.
- <span class="highlight-magenta">Línea 7:</span> El `print()` vacío genera el enter/salto a la siguiente línea del terminal una vez que terminamos de dibujar esa fila."""
new_nested_exp = """- <span class="highlight-blue">Línea 4:</span> `range(altura, 0, -1)` itera en reversa desde `5` hasta `1`.
- <span class="highlight-orange">Línea 5:</span> El ciclo interno depende de la `fila` actual. En la primera iteración, al valer `5`, este ciclo se ejecuta 5 veces.
- <span class="highlight-magenta">Línea 7:</span> El `print()` vacío genera el enter/salto a la siguiente línea del terminal una vez que terminamos de dibujar esa fila."""
content = content.replace(old_nested_exp, new_nested_exp)

# Replace Python Shortcut Code Block
old_shortcut = """```python {all|1-2|4-5|1-5}
altura = 5
print("Método 2: Multiplicación de Strings")

for fila in range(1, altura + 1):
    print("* " * fila)
```"""
new_shortcut = """```python {all|1-2|4-5|1-5}
altura = 5
print("Método 2: Multiplicación de Strings")

for fila in range(altura, 0, -1):
    print("* " * fila)
```"""
content = content.replace(old_shortcut, new_shortcut)

with open('slides_ejercicios.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("¡Triángulo invertido configurado!")
