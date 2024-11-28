# Importar las librerías necesarias
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Cargar el dataset desde el repositorio de GitHub
file_path ="wine.csv"
df = pd.read_csv(url)

# Mostrar las primeras filas del DataFrame
print(df.head())

# Seleccionar características y objetivo
# Supongamos que usamos 'volatile acidity' y 'citric acid' como características
# y 'quality' como objetivo (puedes ajustar las columnas según lo que necesites)
X = df[['volatile acidity', 'citric acid']].values
y = df['quality'].values

# Crear un gráfico 3D con Plotly (si los datos lo permiten)
fig = px.scatter_3d(df, x='volatile acidity', y='citric acid', z='quality', title="Scatter 3D: Wine Quality")
fig.show()

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3)

# Crear un modelo de regresión lineal
lr = LinearRegression()
lr.fit(X_train, y_train)

# Predecir en los datos de prueba
y_pred = lr.predict(X_test)

# Calcular y mostrar las métricas de evaluación
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 score:", r2_score(y_test, y_pred))
