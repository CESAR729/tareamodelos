import pandas as pd

# Especifica el archivo CSV
csv_file = 'Casos_Anemia_Region_Cusco_2010_2020_Cusco.csv'

# Intenta leer el archivo CSV con el delimitador adecuado
try:
    df = pd.read_csv(csv_file, sep=';')  # Cambia 'sep' si el delimitador es diferente
except Exception as e:
    print(f"Error al leer el archivo CSV: {e}")
    exit()

# Convierte el DataFrame a una tabla Markdown
try:
    from tabulate import tabulate
    markdown_table = tabulate(df, headers='keys', tablefmt='pipe', showindex=False)
except ImportError:
    raise ImportError("Por favor instala la biblioteca 'tabulate' con: pip install tabulate")

# Agrega la tabla al README.md
try:
    with open('README.md', 'a', encoding='utf-8') as f:  # 'a' agrega al final del archivo
        f.write("\n## Casos de Anemia en la Región Cusco (2010-2020)\n\n")  # Título descriptivo
        f.write(markdown_table + "\n")
    print("Contenido del archivo CSV agregado al README.md")
except Exception as e:
    print(f"Error al escribir en README.md: {e}")
