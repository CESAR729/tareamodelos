# Análisis y Visualización de Datos Químicos y Categóricos del Dataset *Wine*

Este proyecto tiene como objetivo analizar y visualizar el conjunto de datos *Wine* de la biblioteca `sklearn`. Se realiza un estudio detallado de las características químicas de los vinos y su clasificación en tres categorías distintas.

---

## Integrantes

| Nombre                                  | Código   |
|-----------------------------------------|----------|
| Elbert Cesar Sanchez Chacon             | 200341   |
| Jose Antonio Sullca Aquino              | 183485   |
| Wilfredo Chino Choquenaira              | 141002   |
| Cesar Aparicio Condori Huaychay         | 154628   |

---

## Objetivo del Proyecto

Analizar las características químicas y cualitativas de diferentes tipos de vino mediante herramientas de Python. Este análisis incluye la visualización inicial del dataset, exploración de las relaciones entre las variables, y una mejor comprensión de su estructura.

---

## Descripción del Dataset

El conjunto de datos *Wine* proviene de la biblioteca `sklearn` y contiene información sobre vinos clasificados en tres categorías. Cada vino está descrito mediante 13 características químicas y una categoría (`class`). A continuación, se definen las características incluidas:

### Características Químicas:
- **Alcohol**: Porcentaje de alcohol presente en el vino.
- **Malic acid**: Cantidad de ácido málico (componente orgánico).
- **Ash**: Contenido de cenizas del vino.
- **Alcalinity of ash**: Alcalinidad medida en las cenizas.
- **Magnesium**: Nivel de magnesio (mg/L).
- **Total phenols**: Cantidad total de compuestos fenólicos.
- **Flavanoids**: Subgrupo de compuestos fenólicos que afectan el sabor.
- **Nonflavanoid phenols**: Fenoles no flavonoides presentes.
- **Proanthocyanins**: Componentes responsables del color del vino.
- **Color intensity**: Intensidad del color del vino.
- **Hue**: Tono del color del vino.
- **OD280/OD315 of diluted wines**: Relación de absorbancia, indicando calidad.
- **Proline**: Cantidad de prolina, un aminoácido.

### Variable de Categoría:
- **Class**: Clasificación del vino en tres tipos diferentes, identificados como:
  - Clase 0
  - Clase 1
  - Clase 2

---

## Scripts Disponibles

### Visualizar las primeras filas del conjunto de datos

Este script permite cargar y visualizar las primeras cinco filas del dataset para entender su estructura básica.

#### Código:

```python
from sklearn.datasets import load_wine
import pandas as pd

# Cargar el dataset
wine = load_wine()
df = pd.DataFrame(data=wine.data, columns=wine.feature_names)
df['class'] = wine.target

# Visualizar primeras filas
print(df.head())
