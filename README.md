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
- Python 3.8+
- Bibliotecas:
  - pandas
  - matplotlib
  - seaborn
"""

# Importación de bibliotecas necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración global para gráficos
sns.set_theme(style="whitegrid")
plt.rcParams["figure.dpi"] = 100

# Función principal
def main():
    # Ruta del archivo CSV (cambiar según la ubicación)
    file_path = "cobertura_agua_potable_cusco_2016_2019.csv"
    
    # Carga de datos
    try:
        data = pd.read_csv(file_path)
        print("Datos cargados exitosamente.\n")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta especificada: {file_path}")
        return

    # Resumen de datos
    show_basic_info(data)
    
    # Generación de análisis y visualizaciones
    plot_coverage_evolution(data)
    plot_coverage_distribution(data)
    plot_population_vs_users(data)
    
    # Guardar resumen estadístico
    save_summary(data)

# Función para mostrar información básica de los datos
def show_basic_info(data):
    print("Primeros registros del conjunto de datos:")
    print(data.head(), "\n")
    print("Resumen estadístico:")
    print(data.describe(), "\n")

# Gráfico 1: Evolución de la cobertura por año
def plot_coverage_evolution(data):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x="Año de Medición", y="Cobertura de Agua Potable (%)", 
                 hue="Nombre de la Localidad", marker="o")
    plt.title("Evolución de la Cobertura de Agua Potable en Cusco (2016-2019)")
    plt.xlabel("Año")
    plt.ylabel("Cobertura (%)")
    plt.legend(title="Localidad", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.show()

# Gráfico 2: Distribución de la cobertura
def plot_coverage_distribution(data):
    plt.figure(figsize=(8, 6))
    sns.histplot(data["Cobertura de Agua Potable (%)"], kde=True, bins=15, color="skyblue")
    plt.title("Distribución de la Cobertura de Agua Potable (%)")
    plt.xlabel("Cobertura (%)")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()

# Gráfico 3: Relación entre población total y usuarios atendidos
def plot_population_vs_users(data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x="Población Total", y="Usuarios Atendidos", 
                    hue="Año de Medición", size="Cobertura de Agua Potable (%)", 
                    sizes=(20, 200), palette="viridis")
    plt.title("Relación entre Población Total y Usuarios Atendidos")
    plt.xlabel("Población Total")
    plt.ylabel("Usuarios Atendidos")
    plt.legend(title="Año de Medición", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.show()

# Función para guardar el resumen estadístico
def save_summary(data):
    output_file = "resumen_cobertura_agua_potable.csv"
    data.describe().to_csv(output_file)
    print(f"Resumen estadístico guardado en: {output_file}")

# Ejecución del script principal
if __name__ == "__main__":
    main()
