# Importar las bibliotecas necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV con los datos de RENIEC
archivo_csv = 'registro_hechos_vitales.csv'  # Reemplaza con la ruta de tu archivo CSV
df = pd.read_csv(archivo_csv)

# Verificar las primeras filas del dataframe para asegurarnos de que los datos se cargaron correctamente
print(df.head())

# Asegurarnos de que las columnas están correctamente nombradas y los tipos de datos son los correctos
print(df.columns)

# Calcular la cantidad de nacimientos, matrimonios y defunciones por región o zona
df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')  # Asegurarse de que 'Fecha' esté en formato datetime

# Filtrar los eventos por tipo: Nacimiento, Matrimonio, Defunción
eventos = df['Tipo de Evento'].unique()
print("Tipos de eventos disponibles:", eventos)

# Calcular la cantidad de eventos por tipo y por región
df_eventos_regionales = df.groupby(['Región', 'Tipo de Evento']).size().reset_index(name='Cantidad de Eventos')

# Graficar la cantidad de nacimientos, matrimonios y defunciones por región
plt.figure(figsize=(14, 7))

# Graficar cantidad de eventos por tipo
sns.barplot(x='Región', y='Cantidad de Eventos', hue='Tipo de Evento', data=df_eventos_regionales)
plt.title('Cantidad de Nacimientos, Matrimonios y Defunciones por Región')
plt.xticks(rotation=45, ha='right')

# Mostrar la gráfica
plt.tight_layout()
plt.show()

# Análisis de las estadísticas descriptivas para los eventos
print("\nEstadísticas descriptivas de la cantidad de eventos por tipo y región:")
print(df_eventos_regionales.describe())

# Análisis de la cantidad de eventos a lo largo del tiempo (por año)
df['Año'] = df['Fecha'].dt.year  # Extraer el año de la fecha
eventos_anuales = df.groupby(['Año', 'Tipo de Evento']).size().reset_index(name='Cantidad de Eventos')

# Graficar la evolución de los eventos a lo largo del tiempo
plt.figure(figsize=(14, 7))
sns.lineplot(x='Año', y='Cantidad de Eventos', hue='Tipo de Evento', data=eventos_anuales)
plt.title('Evolución de Nacimientos, Matrimonios y Defunciones a lo Largo del Tiempo')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
