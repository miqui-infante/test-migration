# Proyecto de Migración a Monorepo

## Objetivo

Este espacio de trabajo se utiliza para realizar pruebas antes de una migración masiva de múltiples repositorios a un monorepo.

## Fase Inicial: Verificación de Estado

El objetivo inicial es comprobar el estado de los repositorios a migrar, intentando:
1. Descargar cada repositorio
2. Intentar compilarlo según su tipología
3. Registrar el estado de compilación

## Listado de Repositorios

Los repositorios a procesar se encuentran en:
```
/Users/miqui/git/masorange/deprecation.csv
```

### Estructura del archivo
```
nombre-repo,estado
```

Donde:
- `nombre-repo`: Nombre del repositorio
- `estado`: Puede ser `""` (vacío) o `"deprecated"`

## Clonado de Repositorios

### Organización
Todos los repositorios pertenecen a la organización **masorange** en GitHub.

### Credenciales
Las credenciales de GitHub están cacheadas, por lo que no es necesario especificarlas.

### Comando de clonado
```bash
git clone https://github.com/masorange/{nombre-repo}
```

### Ubicación temporal
Todos los repositorios clonados se almacenarán en:
```
./tmp/
```

## Compilación de Proyectos

### Convención de Nombres

Todos los repositorios siguen la convención:
```
gea-<carpeta>-<ptype>-<proyecto>[-<sufijo>]
```

Donde:
- `gea`: Valor fijo. Corresponde al dominio GEA (del área Big Data & Analytics)
- `<carpeta>`: Ownership/contribution (uc, arc, com)
- `<ptype>`: Tipo de proyecto (mir, gra, pyd, etc.)
- `<proyecto>`: Nombre específico del proyecto (antes denominado productId)
- [`-<sufijo>`]: Opcional. Sufijos como `-workflows`, `-jobs`, etc. que indican la función del proyecto

### Reglas de Compilación por Tipología

La tipología se determina extrayendo el campo `<ptype>` del nombre del repositorio:

- **Proyectos tipo "mir"**: Se compilan con `./gradlew bottle`
- **Resto de proyectos**: Se compilan con `./gradlew build`

## Requisitos Técnicos

### Entorno Virtual Python
Existe un entorno virtual Python con las dependencias necesarias en:
```
~/venvs/monorepper
```

**IMPORTANTE**: Todos los scripts de prueba deben ejecutarse dentro de este entorno virtual.

### Convención para Scripts
Todos los scripts deben crearse en la carpeta **`src/`**.

Cada script debe crearse en dos archivos:

1. **`src/{nombre}.py`**: Script Python con la lógica de negocio
2. **`src/{nombre}.sh`**: Script Bash que:
   - Carga el entorno virtual
   - Invoca al script Python correspondiente

**Ejemplo de estructura**:
```bash
# src/{nombre}.sh
#!/bin/bash

# Obtener la ruta del directorio donde está este script
SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

source ~/venvs/monorepper/bin/activate
python ${SRC_DIR}/{nombre}.py
```

**Nota**: Los scripts deben obtener su propia ubicación (`SRC_DIR`) para poder ejecutarse desde cualquier directorio especificando la ruta completa.

### Sistema de Logging y Reportes

**IMPORTANTE**: Todos los scripts Python deben seguir estas normas obligatorias:

#### 1. Logging Dual (stdout + archivo)
Cada script debe implementar un sistema de logging que escriba **simultáneamente**:
- A la salida estándar (stdout) para seguimiento en tiempo real
- A un archivo de log en la carpeta `logs/`

**Convención de nombres de log**:
```
logs/{nombre-script}-{YYYYMMDD-HHmmss}.txt
```

#### 2. Generación de Reportes
Todos los reportes markdown deben generarse en la carpeta **`output/`**.

**Convención de nombres de reporte**:
```
output/{nombre-script}.md
```

#### 3. Estructura de Carpetas del Proyecto
```
.
├── src/              # Scripts Python y Bash
├── logs/             # Logs de ejecución (auto-generada)
├── output/           # Reportes markdown (auto-generada)
├── tmp/              # Repositorios clonados (temporal)
└── CLAUDE.md         # Este documento
```

## Fase II: Compilación de Proyectos MIR

### Objetivo
Comprobar la compilación de los proyectos de tipología MIR (workflows Mirinda) que pertenezcan a casos de uso activos.

### Proceso de Filtrado
A partir del archivo `deprecation.csv`, se aplicarán los siguientes filtros en orden:

1. **Total de proyectos**: Leer todos los repositorios del archivo
2. **Filtro por carpeta**: Seleccionar solo proyectos con `<carpeta> = uc` (casos de uso)
   - Patrón: `gea-uc-*`
3. **Filtro por tipología**: Seleccionar solo proyectos con `<ptype> = mir`
   - Patrón: `gea-uc-mir-*`
4. **Filtro por estado**: Excluir proyectos marcados como `"deprecated"`
   - Solo proyectos activos (estado vacío)

### Flujo de Ejecución
Para cada proyecto que pase los filtros:

1. Limpiar carpeta `./tmp/{nombre-repo}` si existe
2. Clonar el repositorio en `./tmp/{nombre-repo}`
3. Compilar con `./gradlew bottle`
4. Registrar el resultado (éxito/fallo)
5. Si falla, capturar el mensaje de error

### Reporte: output/fase2.md

Se generará un archivo `output/fase2.md` con la siguiente estructura:

```markdown
# Compilación proyectos MIR

## Resumen Ejecutivo
- Total de proyectos: P
- Total de proyectos de Casos de Uso: U
- Total de proyectos MIR en uc: X
- Proyectos activos (no deprecated): Y
- Proyectos que compilan correctamente: Z
- Tasa de éxito: Z/Y (XX%)

## Proyectos que NO compilan
- nombre-repo-1
- nombre-repo-2
- ...

## Detalle de errores

### nombre-repo-1

[Mensaje de error de compilación]

### nombre-repo-2

[Mensaje de error de compilación]

```

### Resultado Esperado
Un informe completo del estado de compilación de todos los proyectos MIR activos de casos de uso,
identificando aquellos que requieren corrección antes de la migración al monorepo, y el fichero de log.

1. **Reporte final**: `output/fase2.md`
- Resumen ejecutivo con estadísticas
- Lista de proyectos que no compilan
- Detalle de errores de compilación

2.  **Log de ejecución**: `logs/fase2-{YYYYMMDD-HHmmss}.txt`
- Contiene toda la salida del script
- Persiste aunque se interrumpa la ejecución

