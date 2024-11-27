# Importar las librerías necesarias
from sklearn.datasets import make_regression
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Generar datos de regresión
X, y = make_regression(n_samples=100, n_features=2, n_informative=2, n_targets=1, noise=50)

# Crear un DataFrame con los datos
df = pd.DataFrame({'feature1': X[:, 0], 'feature2': X[:, 1], 'target': y})

# Mostrar las primeras filas del DataFrame
print(df.head())

# Crear un gráfico 3D con Plotly
fig = px.scatter_3d(df, x='feature1', y='feature2', z='target')
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
