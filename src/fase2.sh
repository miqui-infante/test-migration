#!/bin/bash

# Script para ejecutar la Fase II con el entorno virtual Python
# Carga el virtualenv monorepper y ejecuta el script fase2.py

# Obtener la ruta del directorio donde está este script
SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Activando entorno virtual monorepper..."
source ~/venvs/monorepper/bin/activate

echo "Ejecutando fase2.py..."
python ${SRC_DIR}/fase2.py

echo "Proceso completado."
