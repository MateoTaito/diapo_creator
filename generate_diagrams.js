const plantumlEncoder = require('plantuml-encoder');
const fs = require('fs');
const https = require('https');
const path = require('path');

const outputDir = path.join(__dirname, 'Clase_1707', 'diagramas');

if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}

const diagrams = [
  {
    name: '01-estructura-programa',
    content: `@startuml
skinparam backgroundColor white
skinparam defaultFontSize 12
skinparam dpi 150
skinparam defaultFontName Arial
start
:Archivo .py;
note right
  ZONA 1: imports
  ZONA 2: def nombre_funcion()
  ZONA 3: programa principal
end note
partition "ZONA 1: imports" {
  :import random;
}
partition "ZONA 2: funciones" {
  :def saludar();
  :def mostrar_menu();
}
partition "ZONA 3: main" {
  :mostrar_menu();
  :saludar();
}
stop
@enduml`
  },
  {
    name: '02-definicion-funcion',
    content: `@startuml
skinparam backgroundColor white
skinparam defaultFontSize 13
skinparam dpi 150
skinparam defaultFontName Arial
start
:def saludar();
note right
  def = palabra clave
  saludar = nombre (verbo)
  () = parametros (vacio)
  : = fin de la firma
end note
:block indentado;
note right
  print("Hola")
  print("Chao")
end note
stop
@enduml`
  },
  {
    name: '03-llamada-funcion',
    content: `@startuml
skinparam backgroundColor white
skinparam defaultFontSize 12
skinparam dpi 150
skinparam defaultFontName Arial
start
:Programa principal;
:Ejecutar saludar();
note right
  El flujo "entra" a la funcion
end note
:Ejecutar bloque de saludar();
:Volver al programa principal;
:Continuar con la siguiente linea;
stop
@enduml`
  },
  {
    name: '04-flujo-entradas-salidas',
    content: `@startuml
skinparam backgroundColor white
skinparam defaultFontSize 12
skinparam dpi 150
skinparam defaultFontName Arial
start
:Programa principal;
:Argumento: nombre = "Ana";
:Argumento: edad = 20;
note right
  ENTRADAS (parametros)
end note
:Ejecutar saludar_persona(nombre, edad);
:Funcion procesa datos;
:return saludo;
note right
  SALIDA (return)
end note
:Programa principal recibe saludo;
:Continuar ejecucion;
stop
@enduml`
  },
  {
    name: '05-scope-variables',
    content: `@startuml
skinparam backgroundColor white
skinparam defaultFontSize 12
skinparam dpi 150
skinparam defaultFontName Arial
start
partition "Scope Global" {
  :Variable: x = 5;
  note right
    Existe en todo
    el archivo
  end note
}
partition "Scope Local (funcion_a)" {
  :Variable: mensaje = "Hola";
  note right
    SOLO existe dentro
    de la funcion
  end note
  :print(mensaje);
  :Fin de funcion_a;
  note right
    mensaje se elimina
  end note
}
partition "Scope Local (funcion_b)" {
  :Variable: y = 10;
  note right
    No tiene acceso a
    mensaje de A
  end note
}
stop
@enduml`
  },
  {
    name: '06-mutabilidad-listas',
    content: `@startuml
skinparam backgroundColor white
skinparam defaultFontSize 12
skinparam dpi 150
skinparam defaultFontName Arial
start
partition "Programa principal" {
  :lista = [1, 2, 3];
  note right
    MISMA referencia
    en memoria
  end note
}
partition "Funcion agregar(lista, elem)" {
  :lista.append(elem);
  note right
    Modifica la MISMA
    lista, no una copia
  end note
  :print(f"Dentro: {lista}");
}
partition "Programa principal" {
  :print(f"Fuera: {lista}");
  note right
    El cambio PERSISTE
    afuera de la funcion
  end note
}
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
