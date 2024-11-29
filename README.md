# Dataset Wine

Este proyecto utiliza el conjunto de datos *Wine* de la biblioteca `sklearn` para análisis y visualización. Se incluyen los scripts necesarios para cargar, explorar y visualizar el conjunto de datos.

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

El objetivo de este proyecto es analizar el conjunto de datos *Wine* mediante herramientas de Python, permitiendo explorar sus características y estructura para un mejor entendimiento de su composición.

---

## Dataset: *Wine*

El conjunto de datos *Wine* contiene información química y cualitativa sobre diferentes tipos de vino. Cada muestra está clasificada en una de tres categorías (`class`). Los datos incluyen las siguientes características:

- **Alcohol**
- **Malic acid**
- **Ash**
- **Alcalinity of ash**
- **Magnesium**
- **Total phenols**
- **Flavanoids**
- **Nonflavanoid phenols**
- **Proanthocyanins**
- **Color intensity**
- **Hue**
- **OD280/OD315 of diluted wines**
- **Proline**

---

## Scripts Disponibles

### Visualizar las primeras filas del conjunto de datos

El script permite cargar el conjunto de datos y mostrar las primeras filas para obtener una visión general de la estructura de los datos.

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
