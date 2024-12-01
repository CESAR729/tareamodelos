import pandas as pd

# Lista de archivos CSV
csv_files = ['ubigeo_departamento.csv', 'ubigeo_provincia.csv', 'ubigeo_distrito.csv']

# Cargar los archivos CSV y agregar sus tablas al README.md
try:
    from tabulate import tabulate
except ImportError:
    raise ImportError("Por favor instala la biblioteca 'tabulate' con: pip install tabulate")

# Ruta del archivo README.md
readme_file = 'README.md'

with open(readme_file, 'a', encoding='utf-8') as f:  # Modo 'a' para agregar al archivo existente
    for csv_file in csv_files:
        try:
            # Carga el archivo CSV (ajusta el delimitador si es necesario)
            df = pd.read_csv(csv_file, sep=';')
            
            # Convierte el DataFrame a una tabla Markdown
            markdown_table = tabulate(df, headers='keys', tablefmt='pipe', showindex=False)
            
            # Escribe la tabla en el README.md
            f.write(f"\n## Contenido de {csv_file}\n\n")  # Título para cada tabla
            f.write(markdown_table + "\n")
            print(f"Contenido de {csv_file} agregado al README.md")
        except Exception as e:
            print(f"Error al procesar {csv_file}: {e}")

print("Proceso completado.")
