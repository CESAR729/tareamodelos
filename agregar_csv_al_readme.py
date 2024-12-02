import pandas as pd

# Ruta del archivo CSV
csv_file = 'Casos_Anemia_Region_Cusco_2010_2020_Cusco .csv'  # Cambia por la ruta correcta de tu archivo CSV

# Intentamos leer el archivo con una codificación diferente
try:
    df = pd.read_csv(csv_file, sep=';', encoding='ISO-8859-1')  # Alternativa a 'latin1'
except UnicodeDecodeError:
    print("Error de codificación. Intenta con otra codificación.")
    
# Convierte el DataFrame a una tabla Markdown
try:
    from tabulate import tabulate
    markdown_table = tabulate(df, headers='keys', tablefmt='pipe', showindex=False)
except ImportError:
    raise ImportError("Por favor instala la biblioteca 'tabulate' con: pip install tabulate")

# Guarda la tabla Markdown en el README.md
with open('README.md', 'a', encoding='utf-8') as f:
    f.write("\n## Contenido del archivo CSV\n\n")  # Agrega un título para la tabla
    f.write(markdown_table + "\n")

print("Contenido del archivo CSV agregado al README.md")
