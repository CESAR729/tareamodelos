import os
import pandas as pd
from tabulate import tabulate

# Lista de archivos CSV con las rutas correctas
csv_files = [r'C:\Users\User\Documents\GitHub\tareamodelos\ubigeo_departamento.csv',
             r'C:\Users\User\Documents\GitHub\tareamodelos\ubigeo_provincia.csv',
             r'C:\Users\User\Documents\GitHub\tareamodelos\ubigeo_distrito.csv']

# Ruta del archivo README.md
readme_file = r'C:\Users\User\Documents\GitHub\tareamodelos\README.md'

# Verificar si los archivos existen antes de procesarlos
for csv_file in csv_files:
    if not os.path.exists(csv_file):
        print(f"Error: El archivo {csv_file} no existe en la ruta especificada.")
        continue  # Saltar al siguiente archivo si no existe

    try:
        # Cargar el archivo CSV (ajusta el delimitador si es necesario)
        df = pd.read_csv(csv_file, sep=';')

        # Convierte el DataFrame a una tabla Markdown
        markdown_table = tabulate(df, headers='keys', tablefmt='pipe', showindex=False)

        # Escribe la tabla en el README.md
        with open(readme_file, 'a', encoding='utf-8') as f:  # Modo 'a' para agregar al archivo existente
            f.write(f"\n## Contenido de {csv_file}\n\n")  # Título para cada tabla
            f.write(markdown_table + "\n")
        
        print(f"Contenido de {csv_file} agregado al README.md")

    except Exception as e:
        print(f"Error al procesar {csv_file}: {e}")

print("Proceso completado.")
