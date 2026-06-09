#!/bin/bash

# Script para ejecutar la Fase I con el entorno virtual Python
# Carga el virtualenv monorepper y ejecuta el script fase1.py

# Obtener la ruta del directorio donde está este script
SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Activando entorno virtual monorepper..."
source ~/venvs/monorepper/bin/activate

echo "Ejecutando fase1.py..."
python ${SRC_DIR}/fase1.py

echo "Proceso completado."
