import pandas as pd
from tabulate import tabulate

# Ruta al archivo CSV (ajustada a la ubicación absoluta)
csv_file = r"C:\Users\User\Documents\OtroDirectorio\Casos_Anemia_Region_Cusco_2010_2020_Cusco.csv"

# Lee el archivo CSV
try:
    df = pd.read_csv(csv_file, sep=';', encoding='utf-8')  # Ajusta 'sep' o 'encoding' si es necesario
except FileNotFoundError:
    print(f"Error: El archivo '{csv_file}' no se encuentra en el directorio especificado.")
    exit(1)
except pd.errors.ParserError as e:
    print(f"Error al leer el archivo CSV: {e}")
    exit(1)

# Convierte el DataFrame a una tabla Markdown
try:
    markdown_table = tabulate(df, headers='keys', tablefmt='pipe', showindex=False)
except ImportError:
    raise ImportError("Por favor instala la biblioteca 'tabulate' con: pip install tabulate")

# Guarda la tabla Markdown en el README.md
try:
    with open('README.md', 'a', encoding='utf-8') as f:  # Modo 'a' para agregar al final del archivo existente
        f.write("\n## Contenido del archivo CSV\n\n")  # Agrega un título para la tabla
        f.write(markdown_table + "\n")
    print("Contenido del archivo CSV agregado al README.md")
except Exception as e:
    print(f"Error al escribir en README.md: {e}")
