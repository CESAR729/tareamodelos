# Análisis del Modelo de Árbol de Decisión - Dataset Wine

## Descripción
Este proyecto aplica un modelo de Árbol de Decisión para predecir la clase de vinos en función de diversas características químicas del dataset **Wine**. El modelo es evaluado mediante el **Error Cuadrático Medio (MSE)** y el **Coeficiente de Determinación (R²)**.

## Resultados del Modelo de Árbol de Decisión

### Evaluación del Modelo:
- **Error cuadrático medio (MSE):** 0.16666666666666666
- **Coeficiente de determinación (R²):** 0.7142857142857142

### Gráfica: Predicciones vs. Valores Reales
La siguiente gráfica muestra la relación entre las predicciones realizadas por el modelo y los valores reales en el conjunto de prueba. Idealmente, las predicciones deberían estar cerca de la línea roja discontinua, que representa la igualdad entre las predicciones y los valores reales.

![Predicciones vs. Valores Reales](predicciones_vs_reales.png)

### Visualización del Árbol de Decisión
A continuación, se muestra el árbol de decisión que fue ajustado al dataset. Cada nodo representa una decisión tomada por el modelo basada en las características del vino.

![Árbol de Decisión](arbol_decision.png)

## Conclusión
El modelo de Árbol de Decisión ha mostrado un rendimiento razonable con un **R² de 0.71**, lo que indica que es capaz de explicar aproximadamente el 71% de la variabilidad de los datos. El **MSE de 0.17** sugiere que las predicciones están bastante cercanas a los valores reales, aunque aún podría mejorarse con ajustes adicionales al modelo.
