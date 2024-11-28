import pandas as pd

# Carga el archivo CSV con el delimitador adecuado (puedes cambiar ';' si es diferente)
csv_file = 'Suministros.csv'  # Cambia por la ruta de tu archivo CSV
try:
    df = pd.read_csv(csv_file, sep=';')  # Cambia 'sep' según el delimitador de tu archivo
except FileNotFoundError:
    print(f"Error: El archivo '{csv_file}' no se encontró. Verifica la ruta.")
    exit()
except Exception as e:
    print(f"Error al leer el archivo CSV: {e}")
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

# Guarda la tabla Markdown en el archivo README.md
try:
    with open('README.md', 'a', encoding='utf-8') as f:  # Modo 'a' para agregar al final del archivo existente
        f.write("\n## Contenido del archivo CSV\n\n")  # Agrega un título para la tabla
        f.write(markdown_table + "\n")
    print("Contenido del archivo CSV agregado al README.md")
except Exception as e:
    print(f"Error al escribir en el archivo README.md: {e}")
    exit()
