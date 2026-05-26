const plantumlEncoder = require('plantuml-encoder');
const fs = require('fs');
const https = require('https');
const path = require('path');

const outputDir = path.join(__dirname, 'Clase_2705', 'diagramas');

if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}

const diagrams = [
  {
    name: '01-inicializacion',
    content: `@startuml
skinparam backgroundColor white
skinparam defaultFontSize 11
skinparam dpi 150
skinparam defaultFontName Arial
start
:Crear lista vacía "bosque";
repeat
  :Crear fila vacía;
  repeat
    if (random <= 9?) then (sí)
      :Agregar 1 (árbol);
    else (no)
      :Agregar 2 (fuego);
    endif
    repeat while (¿Más columnas?) is (sí) not (no)
  repeat while (¿Más filas?) is (sí) not (no)
stop
@enduml`
  },
  {
    name: '02-visualizacion',
    content: `@startuml
skinparam backgroundColor white
skinparam defaultFontSize 11
skinparam dpi 150
skinparam defaultFontName Arial
start
:Crear matriz "bosque_visual";
repeat
  :Crear fila vacía;
  repeat
    :Leer bosque[fila][col];
    if (== 0) then (sí)
      :Agregar ".";
    elseif (== 1) then (sí)
      :Agregar "T";
    else
      :Agregar "X";
    endif
    repeat while (¿Más columnas?) is (sí) not (no)
  repeat while (¿Más filas?) is (sí) not (no)
:Imprimir bosque_visual;
stop
@enduml`
  },
  {
    name: '03-vecindario',
    content: `@startuml
skinparam backgroundColor white
skinparam defaultFontSize 11
skinparam dpi 150
skinparam defaultFontName Arial
start
repeat
  repeat
    if (celda == 2?) then (sí)
      if (arriba existe y == 1) then (sí)
        :arriba = 3;
      endif
      if (abajo existe y == 1) then (sí)
        :abajo = 3;
      endif
      if (izq existe y == 1) then (sí)
        :izq = 3;
      endif
      if (der existe y == 1) then (sí)
        :der = 3;
      endif
      :celda = 0;
      :seguir = 0;
    endif
    repeat while (¿Más columnas?) is (sí) not (no)
  repeat while (¿Más filas?) is (sí) not (no)
:Convertir 3 → 2;
stop
@enduml`
  },
  {
    name: '04-nuevo-estado',
    content: `@startuml
skinparam backgroundColor white
skinparam defaultFontSize 11
skinparam dpi 150
skinparam defaultFontName Arial
start
:seguir = 1;
repeat
  repeat
    if (celda == 2?) then (sí)
      :vecinos sanos = 3;
      :celda = 0;
      :seguir = 0;
    endif
    repeat while (¿Más columnas?) is (sí) not (no)
  repeat while (¿Más filas?) is (sí) not (no)
repeat
  repeat
    if (celda == 3?) then (sí)
      :celda = 2;
    endif
    repeat while (¿Más columnas?) is (sí) not (no)
  repeat while (¿Más filas?) is (sí) not (no)
stop
@enduml`
  },
  {
    name: '05-simulacion',
    content: `@startuml
skinparam backgroundColor white
skinparam defaultFontSize 11
skinparam dpi 150
skinparam defaultFontName Arial
start
:seguir = 0;
:iteración = 0;
repeat
  :seguir = 1;
  :Buscar celdas == 2;
  :Marcar vecinos como 3;
  :celdas 2 → 0;
  :celdas 3 → 2;
  :Imprimir bosque;
  :iteración += 1;
  repeat while (seguir == 0?) is (sí) not (no)
:Fin simulación;
stop
@enduml`
  },
  {
    name: '06-diagrama-completo',
    content: `@startuml
skinparam backgroundColor white
skinparam defaultFontSize 11
skinparam dpi 150
skinparam defaultFontName Arial
start
partition "P1: Inicialización" {
  :Crear matriz N×M;
  :Llenar con 1 y 2;
}
partition "P2: Visualización" {
  :Convertir a caracteres;
  :Imprimir bosque;
}
repeat
  partition "P3: Vecindario" {
    :Buscar celdas == 2;
    :Verificar 4 vecinos;
    :Marcar vecinos como 3;
  }
  partition "P4: Nuevo Estado" {
    :celdas 2 → 0;
    :celdas 3 → 2;
  }
  partition "P5: Simulación" {
    :Imprimir estado;
    :iteración += 1;
  }
  repeat while (seguir == 0?) is (sí) not (no)
:Fin: No hay propagación;
stop
@enduml`
  }
];

async function generateDiagrams() {
  for (const diagram of diagrams) {
    const encoded = plantumlEncoder.encode(diagram.content);
    const url = `https://www.plantuml.com/plantuml/png/${encoded}`;
    const outputPath = path.join(outputDir, `${diagram.name}.png`);

    console.log(`Generando ${diagram.name}.png...`);

    await new Promise((resolve, reject) => {
      https.get(url, (res) => {
        if (res.statusCode === 301 || res.statusCode === 302) {
          https.get(res.headers.location, (res2) => {
            const file = fs.createWriteStream(outputPath);
            res2.pipe(file);
            file.on('finish', () => {
              file.close();
              console.log(`  ✓ ${diagram.name}.png generado`);
              resolve();
            });
          }).on('error', reject);
        } else {
          const file = fs.createWriteStream(outputPath);
          res.pipe(file);
          file.on('finish', () => {
            file.close();
            console.log(`  ✓ ${diagram.name}.png generado`);
            resolve();
          });
        }
      }).on('error', reject);
    });
  }
  console.log('\nTodos los diagramas generados correctamente.');
}

generateDiagrams().catch(console.error);
