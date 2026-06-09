# Información del dominio

## Tipología de repos según nombre

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

## Reglas de Compilación por Tipología

- Los proyectos de tipo "mir" se construyen mediante `./gradlew bottle`.
- El resto de proyectos se construyen mediante `./gradlew build`.

