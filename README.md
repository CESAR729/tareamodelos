# Generador de Tablas Markdown desde CSV

Este proyecto permite convertir el contenido de un archivo CSV en una tabla formateada en Markdown y agregarla automáticamente a un archivo `README.md`. Es útil para documentar datos directamente en repositorios de código sin necesidad de procesamiento manual.

## Características
- Carga archivos CSV con delimitadores personalizados.
- Convierte los datos en tablas Markdown utilizando la biblioteca `tabulate`.
- Agrega el contenido procesado al final del archivo `README.md`.

## Requisitos
Antes de ejecutar el script, asegúrate de tener instaladas las siguientes bibliotecas:
- `pandas`
- `tabulate`

Puedes instalarlas utilizando `pip`:

```bash
pip install pandas tabulate
