import pandas as pd
from tabulate import tabulate

# Carga el archivo CSV con el delimitador adecuado (puedes cambiar ';' si es diferente)
csv_file = '/ruta/del/archivo/archivo.csv'  # Actualiza con la ruta correcta
df = pd.read_csv(csv_file, sep=';')  # Ajusta el delimitador según el archivo (por ejemplo, ',' si es CSV estándar)

# Convierte el DataFrame a una tabla Markdown
markdown_table = tabulate(df, headers='keys', tablefmt='pipe', showindex=False)

# Guarda la tabla Markdown en el README.md
with open('README.md', 'a', encoding='utf-8') as f:  # Modo 'a' para agregar al final del archivo existente
    f.write("\n## Contenido del archivo CSV\n\n")  # Agrega un título para la tabla
    f.write(markdown_table + "\n")

print("Contenido del archivo CSV agregado al README.md")
