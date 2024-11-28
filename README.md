import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table

# Cargar el archivo CSV
csv_file = "archivo.csv"  # Cambia esto por la ruta a tu archivo .csv
df = pd.read_csv(csv_file)

# Crear una figura para la tabla
fig, ax = plt.subplots(figsize=(10, 5))  # Ajusta el tamaño de la imagen
ax.axis('off')  # Oculta los ejes

# Crear la tabla
tabla = table(ax, df, loc='center', colWidths=[0.2] * len(df.columns))  # Ajusta el ancho de columnas
tabla.auto_set_font_size(False)
tabla.set_fontsize(12)
tabla.scale(1.2, 1.2)  # Escala para mejorar legibilidad

# Guardar la tabla como imagen
output_image = "tabla.png"  # Nombre de la imagen de salida
plt.savefig(output_image, bbox_inches='tight', dpi=300)
plt.close()

print(f"Imagen guardada como {output_image}")
