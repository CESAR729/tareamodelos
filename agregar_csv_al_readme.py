import pandas as pd

# Nombre del archivo CSV
csv_file = 'aguacusco.csv'

# Carga del archivo CSV
try:
    df = pd.read_csv(csv_file, sep=';')  # Ajusta el delimitador si es necesario
except FileNotFoundError:
    print(f"Error: El archivo '{csv_file}' no se encontró. Verifica la ruta.")
    exit()
except Exception as e:
    print(f"Error al leer el archivo CSV: {e}")
    exit()

# Verifica si el DataFrame tiene datos
if df.empty:
    print("Error: El archivo CSV está vacío o no contiene datos válidos.")
    exit()

# Convierte el DataFrame a una tabla Markdown
try:
    from tabulate import tabulate
    markdown_table = tabulate(df, headers='keys', tablefmt='pipe', showindex=False)
except ImportError:
    print("Error: La biblioteca 'tabulate' no está instalada. Instálala con: pip install tabulate")
    exit()
except Exception as e:
    print(f"Error al convertir el DataFrame a Markdown: {e}")
    exit()

# Escribe la tabla Markdown en el archivo README.md
try:
    with open('README.md', 'a', encoding='utf-8') as f:  # Modo 'a' para agregar contenido
        f.write("\n## Contenido del archivo CSV\n\n")  # Título en Markdown
        f.write(markdown_table + "\n")
    print("Contenido del archivo CSV agregado correctamente a README.md")
except Exception as e:
    print(f"Error al escribir en el archivo README.md: {e}")
    exit()
