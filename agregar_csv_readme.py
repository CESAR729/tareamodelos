import pandas as pd
from tabulate import tabulate
import os

# Especifica la ruta del archivo CSV
csv_file = 'dataset-predial-parcona3.csv'

# Intenta leer el archivo CSV con una codificación diferente
try:
    df = pd.read_csv(csv_file, encoding='ISO-8859-1', sep=';')  # Usar 'ISO-8859-1' para evitar errores de codificación
    if df.empty:
        raise ValueError("El archivo CSV está vacío.")
    print("Archivo cargado exitosamente.")
    print(df.head())  # Verifica las primeras filas del archivo
except Exception as e:
    print(f"Error al leer el archivo CSV: {e}")
    df = None  # Establece df como None si no se puede leer el archivo

# Si df está definido, intenta agregar la tabla a un archivo README.md en formato Markdown
if df is not None:
    try:
        markdown_table = tabulate(df, headers='keys', tablefmt='pipe', showindex=False)

        # Verifica si el archivo README.md existe, si no, lo crea
        if not os.path.exists('README.md'):
            with open('README.md', 'w', encoding='utf-8') as f:  # 'w' crea el archivo si no existe
                f.write("# Proyecto Predial Parcona3\n\n")

        # Agrega la tabla al README.md
        with open('README.md', 'a', encoding='utf-8') as f:  # 'a' agrega al final del archivo
            f.write("\n## Información del Dataset Predial Parcona3\n\n")  # Título descriptivo
            f.write(markdown_table + "\n")
        print("Contenido del archivo CSV agregado al README.md")
    except Exception as e:
        print(f"Error al escribir en README.md: {e}")
else:
    print("El archivo CSV no se pudo cargar, no se agregará la tabla al README.md.")
