# Test Migration - Monorepo Migration Testing

## Descripción

Este proyecto es un espacio de trabajo para realizar pruebas previas a la migración masiva de múltiples repositorios a un monorepo. El objetivo es verificar el estado de compilación de los repositorios existentes antes de consolidarlos en una estructura unificada.

## Objetivo General

Realizar pruebas de compilación y validación de repositorios de la organización **masorange** para:
1. Identificar repositorios que compilan correctamente
2. Detectar repositorios con problemas de compilación
3. Generar reportes detallados del estado de cada repositorio
4. Facilitar la toma de decisiones para la migración al monorepo

## Estructura del Proyecto

```
test-migration/
├── src/              # Scripts de procesamiento
├── logs/             # Logs de ejecución (auto-generada)
├── output/           # Reportes markdown (auto-generada)
├── tmp/              # Repositorios clonados (temporal)
├── CLAUDE.md         # Instrucciones detalladas del proyecto
└── README.md         # Este archivo
```

## Requisitos Previos

### Entorno Virtual Python
Es necesario tener configurado el entorno virtual Python con las dependencias requeridas:
```bash
~/venvs/monorepper
```

### Archivo de Entrada
Los repositorios a procesar se encuentran listados en:
```
/Users/miqui/git/masorange/deprecation.csv
```

Formato del archivo:
```csv
nombre-repo,estado
```

Donde `estado` puede ser vacío (`""`) para repositorios activos o `"deprecated"` para repositorios obsoletos.

## Scripts Disponibles

### Fase I: Descarga y Checkeo de Ramas de Proyectos MIR

**Archivos:**
- `src/fase1.py` - Script principal en Python
- `src/fase1.sh` - Wrapper Bash para ejecutar el script

**Objetivo:**
Descargar los proyectos de tipología MIR (workflows Mirinda) que pertenezcan a casos de uso activos, comprobar su rama por defecto, y generar un csv y un breve reporte.

**Proceso:**
1. Lee el archivo `deprecation.csv`
2. Filtra repositorios con el patrón `gea-uc-mir-*`
3. Excluye repositorios marcados como `deprecated`
4. Clona cada repositorio en `./tmp/`
5. Identifica la rama por defecto de cada repositorio
6. Genera un CSV y un reporte detallado

**Uso:**

```bash
./src/fase1.sh
```

**Salidas:**
- **CSV generado**: `uc-mir-active.csv`
  - Columnas: `name`, `default_branch`
  - Listado de todos los proyectos MIR activos con su rama por defecto

- **Reporte generado**: `output/fase1.md`
  - Resumen ejecutivo con estadísticas
  - Distribución por tipo de rama por defecto (master, develop, main, etc.)
  - Listado completo de repositorios

- **Log de ejecución**: `logs/fase1-{YYYYMMDD-HHmmss}.txt`
  - Registro completo de la ejecución del script

### Fase II: Compilación de Proyectos MIR

**Archivos:**
- `src/fase2.py` - Script principal en Python
- `src/fase2.sh` - Wrapper Bash para ejecutar el script

**Objetivo:**
Compilar todos los proyectos de tipología MIR (workflows Mirinda) activos de casos de uso para verificar su estado de compilación.

**Entrada:**
Esta fase utiliza como entrada el archivo CSV generado por la **Fase I**: `uc-mir-active.csv`

**Proceso:**
1. Lee el archivo `uc-mir-active.csv`
2. Verifica si cada repositorio ya está clonado en `./tmp/`
   - Si no existe, lo clona
   - Si ya existe (por ejemplo, de la Fase I), lo reutiliza
3. Ejecuta `./gradlew bottle` para compilar
4. Genera un reporte detallado

**Uso:**

```bash
./src/fase2.sh
```

**Salidas:**
- **Reporte generado**: `output/fase2.md`
  - Resumen ejecutivo con estadísticas
  - Tasa de éxito de compilación
  - Lista de proyectos que no compilan
  - Detalle de errores de compilación

- **Log de ejecución**: `logs/fase2-{YYYYMMDD-HHmmss}.txt`
  - Registro completo de la ejecución del script

## Notas

- Los repositorios clonados en `./tmp/` son temporales y pueden eliminarse después de cada ejecución
- Las credenciales de GitHub deben estar cacheadas en el sistema
- Se recomienda ejecutar los scripts con suficiente espacio en disco para los clones temporales
