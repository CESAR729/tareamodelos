import pandas as pd

# Ruta al archivo CSV
file_path = 'Casos_Anemia_Region_Cusco_2010_2020_Cusco (3).csv'  # Cambiar si el archivo está en otro directorio
readme_path = 'README.md'

# Cargar el dataset
df = pd.read_csv(file_path, encoding='latin-1', delimiter=';')

# Obtener información básica del dataset
head = df.head().to_markdown(index=False)
columns = df.columns.to_list()
info = str(df.info())

# Crear contenido para el README.md
content = f"""
## Dataset: Casos de Anemia en la Región Cusco (2010-2020)

Este dataset contiene información relacionada con los casos de anemia registrados en la región de Cusco durante los años 2010 a 2020.

### Primeros registros del dataset
```markdown
{head}
