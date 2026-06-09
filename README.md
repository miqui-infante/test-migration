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

### Fase II: Compilación de Proyectos MIR

**Archivos:**
- `src/fase2.py` - Script principal en Python
- `src/fase2.sh` - Wrapper Bash para ejecutar el script

**Objetivo:**
Compilar todos los proyectos de tipología MIR (workflows Mirinda) activos de casos de uso para verificar su estado de compilación.

**Proceso:**
1. Lee el archivo `deprecation.csv`
2. Filtra repositorios con el patrón `gea-uc-mir-*`
3. Excluye repositorios marcados como `deprecated`
4. Clona cada repositorio en `./tmp/`
5. Ejecuta `./gradlew bottle` para compilar
6. Genera un reporte detallado en `fase2.md`

**Uso:**

```bash
./src/fase2.sh
```

**Salida:**
- Reporte generado: `fase2.md`
- Incluye:
  - Resumen ejecutivo con estadísticas
  - Lista de proyectos que no compilan
  - Detalle de errores de compilación

## Notas

- Los repositorios clonados en `./tmp/` son temporales y pueden eliminarse después de cada ejecución
- Las credenciales de GitHub deben estar cacheadas en el sistema
- Se recomienda ejecutar los scripts con suficiente espacio en disco para los clones temporales
