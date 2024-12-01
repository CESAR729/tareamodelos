# Estrategia de Asistencia para Abastecimiento de Agua Potable - “Plan Cisterna”

## Descripción del Proyecto

El **"Plan Cisterna"** es una iniciativa liderada por el [Organismo Técnico de la Administración de los servicios de Saneamiento – OTASS], en colaboración con las Empresas Prestadoras de Servicios (EPS), cuyo objetivo principal es garantizar el abastecimiento de agua potable en zonas críticas a través de la distribución mediante camiones cisterna. Esta estrategia forma parte de los esfuerzos de OTASS para promover el acceso al agua potable en comunidades vulnerables, priorizando la salud y el bienestar social.

Este proyecto corresponde a la **primera etapa de la Estrategia de Asistencia para Abastecimiento de Agua Potable** y se centra en zonas críticas identificadas en diversos departamentos del país.

## Características del Dataset

El dataset asociado a este proyecto consolida información detallada de las actividades realizadas bajo el "Plan Cisterna". Los datos incluyen:

- **Identificación de la actividad:**
  - Nombre de la EPS.
  - Ubicación geográfica (departamento, provincia, distrito).
  - Código Ubigeo para la localización precisa.
  - Coordenadas Este y Norte.

- **Información operativa:**
  - Tipo de servicio prestado.
  - Zona donde se realiza la actividad.
  - Cantidad de agua distribuida (en metros cúbicos).
  - Número de viviendas beneficiadas por la actividad.

- **Información temporal y administrativa:**
  - Fecha de corte para la consolidación de datos.
  - Número de registro único para cada actividad.
  - Año de ejecución.
  - Fecha de registro oficial.

Este conjunto de datos proporciona una visión integral de los esfuerzos realizados en el marco del "Plan Cisterna" y permite un análisis detallado de su impacto.

## Vista Previa del Dataset

El dataset (`agua.csv`) incluye registros representativos de las actividades realizadas. A continuación, se muestra una vista previa:

| Nombre de la EPS      | Departamento | Provincia | Distrito     | Ubigeo | Coordenada Este | Coordenada Norte | Tipo de Servicio  | Zona        | Cantidad Distribuida (m³) | Viviendas Beneficiadas | Fecha de Corte | Número de Registro | Año de Ejecución | Fecha de Registro |
|-----------------------|--------------|-----------|--------------|--------|-----------------|------------------|-------------------|-------------|---------------------------|------------------------|----------------|--------------------|-------------------|-------------------|
| EPS Sedapal           | Lima         | Lima      | Miraflores   | 150122 | -77.034         | -12.121          | Distribución Agua | Zona A      | 50.0                      | 25                     | 2023-01-15     | 001                | 2023              | 2023-01-16        |
| EPS Cusco             | Cusco        | Cusco     | Wanchaq      | 080101 | -71.979         | -13.517          | Distribución Agua | Zona B      | 100.0                     | 50                     | 2023-02-10     | 002                | 2023              | 2023-02-11        |
| EPS Arequipa          | Arequipa     | Arequipa  | Yanahuara    | 040120 | -71.536         | -16.399          | Distribución Agua | Zona C      | 70.0                      | 30                     | 2023-03-05     | 003                | 2023              | 2023-03-06        |

> **Nota:** El contenido completo del dataset está disponible en el archivo `agua.csv`.

## Objetivos del Proyecto

1. **Distribución Eficiente:** Asegurar que el agua potable llegue a las zonas con mayor necesidad.
2. **Monitoreo y Evaluación:** Proveer herramientas para analizar el impacto de las actividades realizadas.
3. **Transparencia:** Facilitar la accesibilidad de los datos al público para fomentar la rendición de cuentas.

## Cómo Usar Este Repositorio

1. **Visualizar los Datos:** 
   Abra el archivo `agua.csv` en su software de análisis preferido, como Excel, Python (pandas), o R.

2. **Analizar el Impacto:** 
   Utilice el dataset para identificar patrones, evaluar el impacto por región, y realizar comparaciones interanuales.

3. **Contribuir:**
   Si tiene sugerencias o mejoras para el proyecto, envíe sus comentarios a través de las herramientas de colaboración de este repositorio.

## Créditos

Este proyecto es desarrollado y gestionado por el [Organismo Técnico de la Administración de los servicios de Saneamiento – OTASS] en colaboración con las EPS del país.

---

¡Gracias por su interés en el "Plan Cisterna"! Si tiene preguntas o desea contribuir, no dude en contactarnos.
