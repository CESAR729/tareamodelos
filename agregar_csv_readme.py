import pandas as pd

# Especifica la ruta del archivo CSV
csv_file = 'Casos_Anemia_Region_Cusco_2010_2020_Cusco.csv'

# Intenta leer el archivo CSV con una codificación diferente
try:
    df = pd.read_csv(csv_file, encoding='ISO-8859-1', sep=';')  # Usar 'ISO-8859-1' para evitar errores de codificación
    print("Archivo cargado exitosamente.")
    print(df.head())  # Verifica las primeras filas del archivo
except Exception as e:
    print(f"Error al leer el archivo CSV: {e}")

# Si deseas agregar la tabla a un archivo README.md en formato Markdown:
try:
    from tabulate import tabulate
    markdown_table = tabulate(df, headers='keys', tablefmt='pipe', showindex=False)

    # Agrega la tabla al README.md
    with open('README.md', 'a', encoding='utf-8') as f:  # 'a' agrega al final del archivo
        f.write("\n## Casos de Anemia en la Región Cusco (2010-2020)\n\n")  # Título descriptivo
        f.write(markdown_table + "\n")
    print("Contenido del archivo CSV agregado al README.md")
except ImportError:
    print("Error: Por favor instala la biblioteca 'tabulate' con: pip install tabulate")
except Exception as e:
    print(f"Error al escribir en README.md: {e}")
