# Indicadores de Cobertura en el Servicio de Agua Potable en el Departamento de Cusco (2016 - 2019)
### [Organismo Supervisor de la Inversión en Infraestructura de Uso Público - OSINERGMIN]

## Integrantes del Proyecto
- **Elbert César Sánchez Chacón** (Código: 200341)
- **José Antonio Sullca Aquino** (Código: 183485)
- **Wilfredo Chino Choquenaira** (Código: 141002)
- **César Condori Huaychay** (Código: 154628)

---

## Descripción del Proyecto
Este proyecto tiene como objetivo analizar los **indicadores de cobertura del servicio de agua potable** en el Departamento de Cusco durante el período 2016-2019. 

Se examinan métricas clave que permiten evaluar:
- El acceso de la población al servicio de agua potable.
- La calidad y continuidad del servicio.
- Las brechas en la cobertura y posibles áreas de mejora.

Los resultados obtenidos buscan apoyar la **planificación estratégica**, el **monitoreo** y la **regulación** del servicio, contribuyendo a garantizar un acceso más **equitativo** y **eficiente** al agua potable en la región de Cusco.

---

## Contenido del Proyecto
### **Archivo CSV**
archivo.csv
### **Análisis y Visualización**
El análisis incluye:
- **Tendencias temporales** en los indicadores de cobertura.
- **Análisis geográfico** para identificar áreas críticas.
- **Evaluación del impacto** de las interrupciones en la continuidad del servicio.

Se presentan visualizaciones interactivas y gráficos que facilitan la interpretación de los datos.

---

## Requerimientos Previos
Para ejecutar el análisis de datos, asegúrate de contar con los siguientes recursos:

### **Software**
- **Python** 3.8 o superior

### **Bibliotecas necesarias**
Instala las bibliotecas requeridas mediante `pip`:
```bash
pip install pandas matplotlib seaborn
# Importar bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV
archivo_csv = "aguacusco.csv"
datos = pd.read_csv(archivo_csv)

# Descripción de los datos
print("Resumen de los datos:")
print(datos.info())

# Visualización básica
sns.lineplot(data=datos, x="Año de Medición", y="Cobertura de Agua Potable (%)", hue="Nombre de la Localidad")
plt.title("Cobertura de Agua Potable en el Departamento de Cusco (2016-2019)")
plt.xlabel("Año")
plt.ylabel("Cobertura (%)")
plt.show()



