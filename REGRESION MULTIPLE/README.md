# Análisis de Regresión Lineal Múltiple con el Dataset Wine

Este proyecto utiliza el **dataset Wine** para realizar una **regresión lineal múltiple**. El objetivo es predecir características químicas de los vinos utilizando las variables disponibles en el dataset.

## Descripción del Proyecto

El **dataset Wine** es un conjunto de datos clásico que contiene información sobre el análisis químico de vinos producidos en la región de Piamonte, Italia. Cada vino se clasifica en función de la variedad de uva de la que proviene, y se espera que el modelo aprenda a distinguir entre las variedades según las propiedades químicas de cada muestra.

### Características del Dataset
- **Instancias:** 178 muestras de vino.
- **Características:** 13 características químicas (todas numéricas).
- **Etiquetas de clase:** 3 clases correspondientes a tres variedades de vino.
  - Clase 0: Vino tipo Barolo.
  - Clase 1: Vino tipo Grignolino.
  - Clase 2: Vino tipo Barbera.

### Variables
- Alcohol
- Ácido málico
- Cenizas
- Alcalinidad de las cenizas
- Magnesio
- Fenoles totales
- Flavonoides
- Fenoles no flavonoides
- Proantocianinas
- Intensidad de color
- Tonalidad
- OD280/OD315 de vinos diluidos
- Prolina

## Instalación

Para ejecutar este proyecto en tu entorno local, primero debes instalar las siguientes librerías:

```bash
pip install scikit-learn pandas matplotlib seaborn
