# Pruebas de Caja Blanca

## Descripción

Este repositorio contiene el desarrollo y la ejecución de pruebas de caja blanca para la función `process(values)`, como parte de una actividad de pruebas de software.

El objetivo es analizar el comportamiento de la función mediante tres tipos de cobertura: cobertura de sentencias (*Statement Coverage*), cobertura de ramas (*Branch Coverage*) y cobertura de caminos (*Path Coverage*).

## Estructura del proyecto

- `process.py`: contiene la función que se evaluará.
- `test_process.py`: contiene los casos de prueba parametrizados con pytest.
- `pytest.ini`: registra los marcadores utilizados para identificar cada tipo de prueba.
- `requirements.txt`: especifica las herramientas necesarias para ejecutar las pruebas.
- `.gitignore`: excluye archivos temporales y el entorno virtual del repositorio.

## Requisitos

Se necesita Python 3 y un entorno virtual para instalar las dependencias del proyecto.

## Instalación

Clonar el repositorio y entrar en la carpeta del proyecto.

Crear el entorno virtual si todavía no existe:

```powershell
python -m venv .venv
```

Activar el entorno virtual en PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
python -m pip install -r requirements.txt
```

## Ejecución de las pruebas

### 1. Cobertura de sentencias

Ejecutar las pruebas asociadas al marcador `statement`:

```powershell
pytest -m statement -v
```

Generar el reporte de cobertura de sentencias:

```powershell
pytest --cov=process --cov-report=term-missing
```

### 2. Cobertura de ramas

Ejecutar las pruebas asociadas al marcador `branch`:

```powershell
pytest -m branch -v
```

Generar el reporte de cobertura de ramas:

```powershell
pytest --cov=process --cov-branch --cov-report=term-missing
```

### 3. Cobertura de caminos

Ejecutar las pruebas asociadas al marcador `path`:

```powershell
pytest -m path -v
```

Generar el reporte de cobertura solicitado para esta etapa:

```powershell
pytest --cov=process --cov-branch --cov-report=term-missing
```

La cobertura de caminos se comprobará mediante el diseño de los casos de prueba y las combinaciones de rutas ejecutadas. `pytest-cov` proporciona métricas de sentencias y ramas, pero no mide directamente la cobertura completa de caminos.

## Control de versiones

Los cambios se registrarán mediante tres commits, uno por cada etapa de cobertura. Finalmente, los commits se sincronizarán con el repositorio remoto mediante Git.

## Autor

Estudiante de Ingeniería en Software y Minería de Datos.