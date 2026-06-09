# Requisitos técnicos

Existe un entorno virtual python en ~/venvs/monorepper en el que se encontrarán las dependencias necesarias para los scripts de pruebas de la migración. Todo script que se cree se deberá ejecutar en dicho venv.

Cada vez que se cree un script nuevo deberá haber un script {nombre}.py y un {nombre}.sh. En el script bash se cargará el entorno virtual y se invocará al script python.

