# **Indicadores de Calidad de Suministro de las Empresas de Distribución Eléctrica a Nivel Nacional (SAIDI, SAIFI)**  
**[Organismo Supervisor de la Inversión en Energía y Minería - OSINERGMIN]**

---

## **Integrantes del Proyecto**  
- **Elbert César Sánchez Chacón** - *200341*  
- **José Antonio Sullca Aquino** - *183485*  
- **Wilfredo Chino Choquenaira** - *141002*  
- **César Condori Huaychay** - *154628*  

---

## **Descripción del Proyecto**  
Este proyecto analiza los indicadores de calidad de suministro eléctrico de las empresas de distribución eléctrica a nivel nacional, con énfasis en los índices **SAIDI** y **SAIFI**, que evalúan:  
- La **duración promedio** de interrupciones en el sistema por usuario (*SAIDI*).  
- La **frecuencia promedio** de interrupciones en el sistema por usuario (*SAIFI*).  

El objetivo es proporcionar información valiosa para monitorear el desempeño de las empresas de distribución eléctrica y apoyar la toma de decisiones regulatorias y operativas.  

---

## **Contenido del Archivo Suministros .CSV**  
import pandas as pd

# Nombre del archivo CSV
csv_file = 'Suministros.csv'

# Carga del archivo CSV
try:
    df = pd.read_csv(csv_file, sep=';')  # Ajusta el delimitador si es necesario
except FileNotFoundError:
    print(f"Error: El archivo '{csv_file}' no se encontró. Verifica la ruta.")
    exit()
except Exception as e:
    print(f"Error al leer el archivo CSV: {e}")
    exit()

# Verifica si el DataFrame tiene datos
if df.empty:
    print("Error: El archivo CSV está vacío o no contiene datos válidos.")
    exit()

# Convierte el DataFrame a una tabla Markdown
try:
    from tabulate import tabulate
    markdown_table = tabulate(df, headers='keys', tablefmt='pipe', showindex=False)
except ImportError:
    print("Error: La biblioteca 'tabulate' no está instalada. Instálala con: pip install tabulate")
    exit()
except Exception as e:
    print(f"Error al convertir el DataFrame a Markdown: {e}")
    exit()

# Escribe la tabla Markdown en el archivo README.md
try:
    with open('README.md', 'a', encoding='utf-8') as f:  # Modo 'a' para agregar contenido
        f.write("\n## Contenido del archivo CSV\n\n")  # Título en Markdown
        f.write(markdown_table + "\n")
    print("Contenido del archivo CSV agregado correctamente a README.md")
except Exception as e:
    print(f"Error al escribir en el archivo README.md: {e}")
    exit()


---

## **Requerimientos Previos**  
Para ejecutar este proyecto, se requiere:  
- **Python 3.8+**  
- Bibliotecas de Python:  
  - `pandas`  
  - `matplotlib`  
  - `seaborn`  

Instala las dependencias ejecutando:  
```bash
pip install pandas matplotlib seaborn
