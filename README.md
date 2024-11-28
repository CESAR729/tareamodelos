"""
Indicadores de Cobertura en el Servicio de Agua Potable en el Departamento de Cusco (2016 - 2019)
[Organismo Supervisor de la Inversión en Infraestructura de Uso Público - OSINERGMIN]

Integrantes del Proyecto:
- Elbert César Sánchez Chacón 200341
- José Antonio Sullca Aquino 183485
- Wilfredo Chino Choquenaira 141002
- César Condori Huaychay 154628

Descripción del Proyecto:
Este proyecto analiza los indicadores de cobertura en el servicio de agua potable en el Departamento de Cusco durante el período 2016-2019. 
Se enfoca en métricas clave para evaluar el acceso y la calidad del servicio brindado a la población, ayudando a identificar brechas en la cobertura y áreas de mejora.

El objetivo principal es generar información que apoye la planificación estratégica, el monitoreo y la regulación para garantizar 
un acceso más equitativo y eficiente al agua potable en la región.

Contenido del Archivo CSV:
El archivo CSV contiene los siguientes campos clave:
1. Nombre de la Localidad: Comunidad o área atendida.
2. Cobertura de Agua Potable (%): Porcentaje de la población con acceso al servicio.
3. Año de Medición: Período en el que se registraron los datos (2016-2019).
4. Población Total: Cantidad de habitantes en la localidad.
5. Usuarios Atendidos: Número de personas con acceso al servicio de agua potable.
6. Volumen Total Distribuido (m³): Cantidad total de agua suministrada.
7. Interrupciones en el Servicio: Número de eventos de interrupción del suministro.
8. Duración de las Interrupciones (horas): Tiempo acumulado de interrupciones.

Requerimientos Previos:
Para ejecutar este proyecto, se requiere:
- Python 3.8+
- Bibliotecas:
  - pandas
  - matplotlib
  - seaborn
"""

# Importación de las bibliotecas necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ruta del archivo CSV (cambia esta ruta según la ubicación de tu archivo)
file_path = "cobertura_agua_potable_cusco_2016_2019.csv"

# Carga de los datos
data = pd.read_csv(file_path)

# Mostrar información básica de los datos
print("Datos cargados:")
print(data.head())

# Resumen estadístico
print("\nResumen estadístico:")
print(data.describe())

# Gráficos principales para el análisis

# Gráfico 1: Evolución de la cobertura por año
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x="Año de Medición", y="Cobertura de Agua Potable (%)", hue="Nombre de la Localidad", marker="o")
plt.title("Evolución de la Cobertura de Agua Potable en Cusco (2016-2019)")
plt.xlabel("Año")
plt.ylabel("Cobertura (%)")
plt.legend(title="Localidad", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico 2: Distribución de la cobertura
plt.figure(figsize=(8, 6))
sns.histplot(data["Cobertura de Agua Potable (%)"], kde=True, bins=15, color="skyblue")
plt.title("Distribución de Cobertura de Agua Potable (%)")
plt.xlabel("Cobertura (%)")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()

# Gráfico 3: Relación entre población total y usuarios atendidos
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x="Población Total", y="Usuarios Atendidos", hue="Año de Medición",
                size="Cobertura de Agua Potable (%)", sizes=(20, 200), palette="viridis")
plt.title("Relación entre Población Total y Usuarios Atendidos")
plt.xlabel("Población Total")
plt.ylabel("Usuarios Atendidos")
plt.legend(title="Año de Medición", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.grid(True)
plt.tight_layout()
plt.show()

# Guardar resumen estadístico en un archivo CSV
output_file = "resumen_cobertura_agua_potable.csv"
data.describe().to_csv(output_file)
print(f"\nResumen estadístico guardado en: {output_file}")
