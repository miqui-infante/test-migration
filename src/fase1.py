#!/usr/bin/env python3
"""
Script para la Fase I: Descarga y Checkeo de Ramas de Proyectos MIR
Filtra proyectos de tipología MIR activos de casos de uso y verifica su rama por defecto.
"""

import csv
import os
import subprocess
import shutil
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import List, Tuple, Dict
from datetime import datetime
from collections import Counter

@dataclass
class RepositoryInfo:
    """Información de un repositorio"""
    name: str
    default_branch: str
    success: bool
    error_message: str = ""

class Logger:
    """Clase para manejar logging tanto a stdout como a archivo"""

    def __init__(self):
        self.log_file = None

    def setup(self):
        """Configura el archivo de log"""
        # Crear carpeta logs si no existe
        os.makedirs("logs", exist_ok=True)

        # Generar nombre de archivo con timestamp
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        log_filename = f"logs/fase1-{timestamp}.txt"

        # Abrir archivo en modo append
        self.log_file = open(log_filename, "w", encoding="utf-8")

        return log_filename

    def print(self, message=""):
        """Imprime tanto a stdout como al archivo de log"""
        # Escribir a stdout
        print(message)

        # Escribir al archivo de log si está configurado
        if self.log_file:
            self.log_file.write(message + "\n")
            self.log_file.flush()  # Asegurar que se escribe inmediatamente

    def close(self):
        """Cierra el archivo de log"""
        if self.log_file:
            self.log_file.close()

class MirProjectScanner:
    """Clase para escanear proyectos MIR y verificar sus ramas por defecto"""

    DEPRECATION_FILE = "/Users/miqui/git/masorange/deprecation.csv"
    TMP_DIR = "./tmp"
    GITHUB_ORG = "masorange"

    def __init__(self, logger: Logger):
        self.logger = logger
        self.total_projects = 0
        self.uc_projects = 0
        self.mir_projects = 0
        self.active_mir_projects = 0
        self.results: List[RepositoryInfo] = []

    def read_repositories(self) -> List[Tuple[str, str]]:
        """Lee el archivo deprecation.csv y devuelve lista de (nombre, estado)"""
        repos = []
        with open(self.DEPRECATION_FILE, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0]:  # Ignorar líneas vacías
                    repo_name = row[0]
                    status = row[1] if len(row) > 1 else ""
                    repos.append((repo_name, status))
        return repos

    def filter_repositories(self, repos: List[Tuple[str, str]]) -> List[str]:
        """
        Aplica los filtros para obtener proyectos MIR activos de casos de uso.
        Retorna lista de nombres de repositorios filtrados.
        """
        self.total_projects = len(repos)

        # Filtro 1: Solo casos de uso (gea-uc-*)
        uc_repos = [(name, status) for name, status in repos if name.startswith("gea-uc-")]
        self.uc_projects = len(uc_repos)

        # Filtro 2: Solo tipología MIR (gea-uc-mir-*)
        mir_repos = [(name, status) for name, status in uc_repos if name.startswith("gea-uc-mir-")]
        self.mir_projects = len(mir_repos)

        # Filtro 3: Excluir deprecated
        active_mir = [name for name, status in mir_repos if status != "deprecated"]
        self.active_mir_projects = len(active_mir)

        return active_mir

    def clone_repository(self, repo_name: str) -> bool:
        """Clona un repositorio en ./tmp/{repo_name}"""
        repo_url = f"https://github.com/{self.GITHUB_ORG}/{repo_name}"
        target_path = os.path.join(self.TMP_DIR, repo_name)

        # Si ya existe, lo eliminamos primero
        if os.path.exists(target_path):
            self.logger.print(f"  Limpiando directorio existente...")
            shutil.rmtree(target_path)

        # Crear directorio tmp si no existe
        os.makedirs(self.TMP_DIR, exist_ok=True)

        self.logger.print(f"  Clonando repositorio...")
        try:
            result = subprocess.run(
                ["git", "clone", repo_url, target_path],
                capture_output=True,
                text=True,
                timeout=300
            )
            return result.returncode == 0
        except subprocess.TimeoutExpired:
            self.logger.print(f"  ⏱️  Timeout al clonar")
            return False
        except Exception as e:
            self.logger.print(f"  ❌ Error al clonar: {e}")
            return False

    def get_current_branch(self, repo_name: str) -> str:
        """Obtiene la rama actual (default branch) del repositorio"""
        target_path = os.path.join(self.TMP_DIR, repo_name)

        try:
            result = subprocess.run(
                ["git", "branch", "--show-current"],
                cwd=target_path,
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                branch = result.stdout.strip()
                return branch if branch else "unknown"
            else:
                return "error"
        except Exception as e:
            self.logger.print(f"  ❌ Error al obtener rama: {e}")
            return "error"

    def process_repository(self, repo_name: str) -> RepositoryInfo:
        """Procesa un repositorio: lo clona y obtiene su rama por defecto"""
        if not self.clone_repository(repo_name):
            return RepositoryInfo(
                name=repo_name,
                default_branch="error",
                success=False,
                error_message="Error al clonar el repositorio"
            )

        default_branch = self.get_current_branch(repo_name)
        self.logger.print(f"  Rama por defecto: {default_branch}")

        return RepositoryInfo(
            name=repo_name,
            default_branch=default_branch,
            success=True
        )

    def generate_csv(self) -> str:
        """Genera el archivo CSV con los resultados"""
        csv_filename = "uc-mir-active.csv"

        with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['name', 'default_branch'])

            for result in self.results:
                if result.success:
                    writer.writerow([result.name, result.default_branch])

        return csv_filename

    def generate_report(self) -> str:
        """Genera el contenido del reporte fase1.md"""
        successful = [r for r in self.results if r.success]

        # Contar distribución por rama
        branch_counter = Counter([r.default_branch for r in successful])

        report = "# Descarga y Checkeo de Ramas - Proyectos MIR\n\n"

        # Resumen Ejecutivo
        report += "## Resumen Ejecutivo\n"
        report += f"- Total de proyectos: {self.total_projects}\n"
        report += f"- Total de proyectos de Casos de Uso: {self.uc_projects}\n"
        report += f"- Total de proyectos MIR en uc: {self.mir_projects}\n"
        report += f"- Proyectos activos (no deprecated): {self.active_mir_projects}\n\n"

        # Distribución por Rama por Defecto
        report += "## Distribución por Rama por Defecto\n"
        for branch, count in sorted(branch_counter.items(), key=lambda x: x[1], reverse=True):
            report += f"- Proyectos con default branch \"{branch}\": {count}\n"
        report += "\n"

        # Listado de Repositorios
        report += "## Listado de Repositorios\n"
        for result in sorted(successful, key=lambda x: x.name):
            report += f"- {result.name} ({result.default_branch})\n"
        report += "\n"

        return report

    def run(self):
        """Ejecuta el proceso completo de la Fase I"""
        self.logger.print("=" * 60)
        self.logger.print("FASE I: Descarga y Checkeo de Ramas - Proyectos MIR")
        self.logger.print("=" * 60)
        self.logger.print()

        # Leer y filtrar repositorios
        self.logger.print("1. Leyendo repositorios...")
        repos = self.read_repositories()

        self.logger.print("2. Aplicando filtros...")
        mir_repos = self.filter_repositories(repos)

        self.logger.print(f"\nRepositorios a procesar: {len(mir_repos)}")
        self.logger.print()

        # Procesar cada repositorio
        for i, repo_name in enumerate(mir_repos, 1):
            self.logger.print(f"[{i}/{len(mir_repos)}] Procesando {repo_name}")
            result = self.process_repository(repo_name)
            self.results.append(result)
            self.logger.print()

        # Generar CSV
        self.logger.print("=" * 60)
        self.logger.print("Generando CSV...")
        csv_filename = self.generate_csv()
        self.logger.print(f"CSV generado en: {csv_filename}")

        # Generar reporte
        self.logger.print("\nGenerando reporte...")
        report_content = self.generate_report()

        # Crear carpeta output si no existe
        os.makedirs("output", exist_ok=True)

        # Guardar reporte en output/fase1.md
        output_file = "output/fase1.md"
        with open(output_file, "w", encoding='utf-8') as f:
            f.write(report_content)

        self.logger.print(f"Reporte generado en: {output_file}")
        self.logger.print("=" * 60)

        # Resumen final
        successful = len([r for r in self.results if r.success])
        failed = len([r for r in self.results if not r.success])
        self.logger.print(f"\n✓ Exitosos: {successful}")
        self.logger.print(f"✗ Fallidos: {failed}")
        self.logger.print(f"Total: {len(self.results)}")
        self.logger.print()

if __name__ == "__main__":
    # Configurar logger
    logger = Logger()
    log_filename = logger.setup()

    print(f"Log guardándose en: {log_filename}")
    print()

    try:
        # Ejecutar scanner
        scanner = MirProjectScanner(logger)
        scanner.run()
    finally:
        # Asegurar que el archivo de log se cierra
        logger.close()
