# **César Condori Huaychay**  
**Estudiante de Ingeniería Informática y de Sistemas**  
**Universidad Nacional de San Antonio Abad del Cusco (UNSAAC)**  

---

# **Registros Electorales en Cusco (2010-2020)**

## **Descripción**
Este proyecto analiza los registros electorales en la región de Cusco durante el período 2010-2020. Se enfoca en estudiar la evolución del padrón electoral, la segmentación demográfica y la proyección de tendencias futuras, utilizando herramientas avanzadas de análisis de datos e inteligencia artificial.

## **Características Principales**
- **Análisis Temporal:** Evaluación de tendencias en el crecimiento del padrón electoral durante la última década.  
- **Segmentación Demográfica:** Comparación de registros según grupos poblacionales (jóvenes, adultos, adultos mayores) y distribución geográfica.  
- **Predicción Basada en AI:** Aplicación de algoritmos de aprendizaje automático para modelar y proyectar comportamientos futuros.  
- **Visualizaciones Interactivas:** Uso de mapas geográficos y gráficos dinámicos para una interpretación clara de los datos.  
- **Análisis Geoespacial:** Evaluación de la distribución de registros electorales a nivel distrital y provincial.

## **Estructura del Proyecto**
El proyecto está organizado en las siguientes carpetas para facilitar su navegación y mantenimiento:

- **`src/`:** Código fuente para análisis, modelado y visualización de datos.  
- **`data/`:** Datos originales y preprocesados sobre los registros electorales.  
- **`casos-de-uso/`:** Documentación detallada sobre las aplicaciones prácticas de los análisis.  
- **`docs/`:** Documentación técnica y conceptual del proyecto.  
- **`notebooks/`:** Notebooks interactivos para explorar y detallar los análisis realizados.  
- **`output/`:** Resultados generados, como gráficos, tablas y reportes.  

## **Instalación**
Sigue los pasos a continuación para configurar y ejecutar el proyecto:

1. Clona este repositorio:  
   ```bash
   git clone https://github.com/tuusuario/Registros-Electorales-Cusco.git
   cd Registros-Electorales-Cusco

## Contenido del archivo CSV

|   ID Elector | Nombre Completo         |      DNI | Provincia     | Distrito       |   Edad | Sexo   |   Mesa de Votación | Dirección            |
|-------------:|:------------------------|---------:|:--------------|:---------------|-------:|:-------|-------------------:|:---------------------|
|            1 | Pedro Ccopa Condori     | 42344811 | Paucartambo   | Kosñipata      |     29 | M      |                 35 | Jr. Los Héroes 880   |
|            2 | Lucía Quispe Flores     | 50063554 | Canchis       | Sicuani        |     73 | F      |                 21 | Pasaje Inca 736      |
|            3 | Lucía Yupanqui Huamán   | 44961373 | La Convención | Quillabamba    |     18 | F      |                 33 | Pasaje Inca 719      |
|            4 | Lucía Ccopa Ccopa       | 20561236 | Canchis       | Sicuani        |     59 | F      |                 27 | Jr. Los Héroes 598   |
|            5 | Luis Chávez Mamani      | 32506233 | Urubamba      | Urubamba       |     48 | M      |                 39 | Pasaje Inca 854      |
|            6 | José Yupanqui Huamán    | 66194188 | Canchis       | San Pablo      |     26 | F      |                 42 | Jr. Los Héroes 252   |
|            7 | María Ccopa Flores      | 22506017 | Calca         | Calca          |     42 | M      |                 39 | Av. Libertad 898     |
|            8 | Juan Ccopa Apaza        | 11761905 | La Convención | Quillabamba    |     63 | M      |                 31 | Urbanización Sol 777 |
|            9 | Lucía Ccopa Yupanqui    | 82201766 | Canchis       | San Pablo      |     38 | F      |                 37 | Urbanización Sol 987 |
|           10 | José Pérez Condori      | 28911365 | La Convención | Quillabamba    |     44 | F      |                  6 | Pasaje Inca 282      |
|           11 | Pedro Quispe Pérez      | 75564843 | Paucartambo   | Colquepata     |     26 | F      |                 41 | Pasaje Inca 645      |
|           12 | Miguel Chávez Apaza     | 11631336 | Paucartambo   | Colquepata     |     39 | F      |                 17 | Pasaje Inca 379      |
|           13 | Ana Quispe Mamani       | 46288588 | Quispicanchi  | Oropesa        |     64 | F      |                 23 | Av. Libertad 334     |
|           14 | Pedro Pérez Quispe      | 93737457 | Calca         | Calca          |     33 | F      |                 46 | Jr. Los Héroes 197   |
|           15 | Miguel Condori Pérez    | 98021884 | Quispicanchi  | Andahuaylillas |     23 | M      |                 31 | Jr. Los Héroes 377   |
|           16 | Carmen Huamán Ccopa     | 55150220 | Quispicanchi  | Andahuaylillas |     38 | M      |                 30 | Pasaje Inca 344      |
|           17 | Carmen Pérez Chávez     | 63337819 | Urubamba      | Machu Picchu   |     66 | F      |                  3 | Pasaje Inca 406      |
|           18 | Luis Yupanqui Apaza     | 13673459 | Quispicanchi  | Oropesa        |     63 | F      |                  4 | Jr. Los Héroes 927   |
|           19 | Carmen Condori Flores   | 14854404 | Urubamba      | Ollantaytambo  |     74 | F      |                 22 | Jr. Los Héroes 384   |
|           20 | María Ccopa Huamán      | 24930906 | Cusco         | Wanchaq        |     32 | M      |                  2 | Pasaje Inca 801      |
|           21 | Rosa Yupanqui Mamani    | 16613403 | La Convención | Echarate       |     29 | F      |                 41 | Jr. Los Héroes 314   |
|           22 | Ana Apaza Quispe        | 14791675 | Quispicanchi  | Oropesa        |     66 | M      |                 47 | Urbanización Sol 568 |
|           23 | Pedro Pérez Apaza       | 41418852 | Calca         | Pisac          |     53 | M      |                  1 | Urbanización Sol 247 |
|           24 | Carmen Apaza Yupanqui   | 86231999 | Paucartambo   | Kosñipata      |     83 | F      |                 16 | Jr. Los Héroes 467   |
|           25 | Lucía Quispe Mamani     | 47999335 | Urubamba      | Machu Picchu   |     58 | M      |                 43 | Calle Principal 405  |
|           26 | Miguel Condori Huamán   | 53005934 | Quispicanchi  | Oropesa        |     51 | F      |                 29 | Calle Principal 372  |
|           27 | Luis Chávez Quispe      | 96000568 | Quispicanchi  | Andahuaylillas |     61 | F      |                 45 | Av. Libertad 18      |
|           28 | Pedro Ccopa Pérez       | 19829005 | La Convención | Santa Teresa   |     79 | M      |                 29 | Av. Libertad 80      |
|           29 | María Apaza Condori     | 83806339 | Quispicanchi  | Andahuaylillas |     43 | M      |                 35 | Av. Libertad 582     |
|           30 | María Ccopa Huamán      | 66015191 | Urubamba      | Urubamba       |     56 | F      |                 46 | Jr. Los Héroes 736   |
|           31 | Carmen Chávez Chávez    | 66427941 | Calca         | Calca          |     63 | F      |                 33 | Calle Principal 763  |
|           32 | Miguel Yupanqui Ccopa   | 78587153 | La Convención | Quillabamba    |     22 | F      |                 27 | Av. Libertad 921     |
|           33 | Luis Ccopa Flores       | 66652359 | Quispicanchi  | Oropesa        |     38 | F      |                 34 | Jr. Los Héroes 549   |
|           34 | Juan Huamán Huamán      | 78831664 | Paucartambo   | Paucartambo    |     73 | M      |                 42 | Calle Principal 159  |
|           35 | Carmen Condori Huamán   | 17815371 | Calca         | Pisac          |     40 | M      |                 11 | Calle Principal 518  |
|           36 | Ana Chávez Flores       | 90358055 | Urubamba      | Machu Picchu   |     38 | M      |                 29 | Urbanización Sol 304 |
|           37 | Lucía Yupanqui Chávez   | 29379345 | Canchis       | Sicuani        |     39 | M      |                 11 | Pasaje Inca 632      |
|           38 | Ana Condori Yupanqui    | 72042566 | Cusco         | Wanchaq        |     83 | M      |                 46 | Jr. Los Héroes 777   |
|           39 | Juan Condori Mamani     | 46025354 | La Convención | Santa Teresa   |     24 | F      |                 49 | Av. Libertad 75      |
|           40 | Rosa Huamán Apaza       | 64441269 | Quispicanchi  | Urcos          |     26 | M      |                 32 | Urbanización Sol 977 |
|           41 | Carmen Flores Yupanqui  | 10813548 | Canchis       | Checacupe      |     75 | F      |                  2 | Urbanización Sol 209 |
|           42 | Rosa Apaza Mamani       | 54590369 | Canchis       | San Pablo      |     47 | F      |                 22 | Av. Libertad 506     |
|           43 | María Huamán Mamani     | 60769933 | Calca         | Lamay          |     23 | F      |                 37 | Av. Libertad 418     |
|           44 | María Chávez Chávez     | 58738416 | La Convención | Santa Teresa   |     84 | F      |                 43 | Calle Principal 767  |
|           45 | Luis Apaza Quispe       | 85751139 | Quispicanchi  | Urcos          |     27 | M      |                 43 | Jr. Los Héroes 756   |
|           46 | Lucía Yupanqui Yupanqui | 29751522 | La Convención | Santa Teresa   |     22 | M      |                  1 | Calle Principal 731  |
|           47 | Lucía Mamani Ccopa      | 97671748 | Quispicanchi  | Urcos          |     61 | M      |                 45 | Jr. Los Héroes 996   |
|           48 | María Apaza Pérez       | 62868449 | Urubamba      | Urubamba       |     40 | F      |                 41 | Av. Libertad 903     |
|           49 | Luis Mamani Condori     | 10647448 | Paucartambo   | Paucartambo    |     29 | F      |                  2 | Jr. Los Héroes 463   |
|           50 | Miguel Apaza Flores     | 54659530 | Paucartambo   | Paucartambo    |     76 | M      |                 14 | Pasaje Inca 126      |
|           51 | Miguel Huamán Ccopa     | 68235968 | Canchis       | Sicuani        |     55 | M      |                 44 | Av. Libertad 314     |
|           52 | Juan Quispe Huamán      | 10842134 | La Convención | Echarate       |     32 | M      |                 15 | Jr. Los Héroes 978   |
|           53 | Miguel Chávez Quispe    | 30798181 | Canchis       | Sicuani        |     53 | M      |                 42 | Av. Libertad 630     |
|           54 | José Ccopa Quispe       | 86839086 | Cusco         | Santiago       |     24 | M      |                 17 | Urbanización Sol 807 |
|           55 | José Chávez Apaza       | 16767844 | La Convención | Quillabamba    |     30 | F      |                 21 | Calle Principal 629  |
|           56 | José Flores Apaza       | 48959795 | Cusco         | Santiago       |     56 | M      |                  8 | Jr. Los Héroes 8     |
|           57 | Carmen Condori Ccopa    | 14311244 | Canchis       | Sicuani        |     65 | M      |                 42 | Jr. Los Héroes 646   |
|           58 | Juan Ccopa Ccopa        | 96846477 | Canchis       | San Pablo      |     27 | M      |                 26 | Urbanización Sol 303 |
|           59 | María Yupanqui Flores   | 46239119 | Calca         | Calca          |     36 | F      |                 30 | Jr. Los Héroes 87    |
|           60 | María Ccopa Flores      | 42587731 | La Convención | Santa Teresa   |     23 | F      |                 30 | Av. Libertad 162     |
|           61 | José Quispe Ccopa       | 62981948 | La Convención | Echarate       |     77 | F      |                 11 | Pasaje Inca 302      |
|           62 | Carmen Pérez Yupanqui   | 74183230 | La Convención | Quillabamba    |     41 | M      |                  6 | Av. Libertad 510     |
|           63 | Pedro Apaza Apaza       | 79432827 | Quispicanchi  | Andahuaylillas |     66 | F      |                  8 | Pasaje Inca 894      |
|           64 | José Apaza Flores       | 75459635 | Quispicanchi  | Andahuaylillas |     77 | F      |                 42 | Calle Principal 850  |
|           65 | Luis Ccopa Condori      | 28284211 | La Convención | Echarate       |     32 | F      |                 27 | Calle Principal 21   |
|           66 | Juan Flores Flores      | 48364589 | Canchis       | San Pablo      |     31 | F      |                 39 | Urbanización Sol 797 |
|           67 | Ana Quispe Apaza        | 21153773 | Quispicanchi  | Oropesa        |     29 | M      |                 17 | Urbanización Sol 984 |
|           68 | Luis Flores Mamani      | 10934268 | Calca         | Pisac          |     48 | F      |                 27 | Calle Principal 832  |
|           69 | Rosa Apaza Yupanqui     | 76837787 | Paucartambo   | Colquepata     |     38 | M      |                 43 | Pasaje Inca 170      |
|           70 | Lucía Huamán Huamán     | 76703658 | Cusco         | Wanchaq        |     80 | F      |                 26 | Pasaje Inca 319      |
|           71 | Ana Ccopa Apaza         | 12189597 | La Convención | Echarate       |     76 | F      |                 38 | Jr. Los Héroes 261   |
|           72 | José Huamán Flores      | 37019383 | Canchis       | Sicuani        |     56 | M      |                  8 | Pasaje Inca 650      |
|           73 | Luis Condori Pérez      | 92786385 | Urubamba      | Machu Picchu   |     35 | M      |                 50 | Calle Principal 282  |
|           74 | Luis Pérez Huamán       | 79179280 | Calca         | Pisac          |     68 | F      |                 49 | Urbanización Sol 340 |
|           75 | José Quispe Flores      | 31538710 | La Convención | Echarate       |     45 | M      |                 43 | Av. Libertad 99      |
|           76 | Juan Mamani Huamán      | 68765727 | Calca         | Pisac          |     46 | F      |                 44 | Pasaje Inca 911      |
|           77 | Rosa Quispe Apaza       | 65954354 | Urubamba      | Urubamba       |     80 | M      |                 19 | Av. Libertad 181     |
|           78 | Ana Yupanqui Huamán     | 26436694 | Urubamba      | Ollantaytambo  |     26 | F      |                  5 | Jr. Los Héroes 30    |
|           79 | Ana Mamani Flores       | 71883709 | Urubamba      | Ollantaytambo  |     80 | F      |                  3 | Urbanización Sol 905 |
|           80 | Luis Flores Flores      | 26156553 | Paucartambo   | Colquepata     |     29 | F      |                  7 | Jr. Los Héroes 876   |
|           81 | Miguel Chávez Apaza     | 11180379 | Quispicanchi  | Oropesa        |     63 | F      |                 29 | Av. Libertad 993     |
|           82 | Juan Mamani Quispe      | 80699664 | Urubamba      | Machu Picchu   |     34 | F      |                 11 | Calle Principal 836  |
|           83 | Pedro Yupanqui Apaza    | 22251025 | Calca         | Calca          |     51 | F      |                 30 | Calle Principal 529  |
|           84 | Ana Quispe Condori      | 99572765 | Quispicanchi  | Andahuaylillas |     36 | F      |                 23 | Av. Libertad 70      |
|           85 | Pedro Apaza Huamán      | 74428326 | Cusco         | Wanchaq        |     75 | F      |                 50 | Urbanización Sol 917 |
|           86 | Lucía Condori Pérez     | 52599310 | Cusco         | Santiago       |     68 | F      |                 27 | Av. Libertad 109     |
|           87 | Lucía Quispe Quispe     | 45809093 | Calca         | Pisac          |     33 | F      |                 48 | Calle Principal 372  |
|           88 | José Mamani Ccopa       | 77298789 | Canchis       | Checacupe      |     47 | F      |                  1 | Av. Libertad 739     |
|           89 | Pedro Chávez Chávez     | 98788220 | Canchis       | San Pablo      |     46 | F      |                 19 | Pasaje Inca 511      |
|           90 | José Pérez Ccopa        | 90974441 | Paucartambo   | Paucartambo    |     42 | F      |                 47 | Av. Libertad 926     |
|           91 | Juan Huamán Quispe      | 20264426 | Paucartambo   | Colquepata     |     51 | F      |                 41 | Pasaje Inca 20       |
|           92 | Rosa Chávez Mamani      | 86735223 | Quispicanchi  | Urcos          |     38 | F      |                 39 | Jr. Los Héroes 36    |
|           93 | Carmen Apaza Condori    | 37514812 | Paucartambo   | Colquepata     |     51 | F      |                 23 | Av. Libertad 696     |
|           94 | Rosa Yupanqui Ccopa     | 49741383 | Calca         | Lamay          |     22 | F      |                 50 | Pasaje Inca 220      |
|           95 | María Flores Apaza      | 29597301 | Calca         | Calca          |     47 | F      |                 34 | Urbanización Sol 474 |
|           96 | Miguel Ccopa Yupanqui   | 26469355 | Quispicanchi  | Urcos          |     53 | M      |                 38 | Pasaje Inca 791      |
|           97 | Ana Pérez Chávez        | 68355425 | Urubamba      | Machu Picchu   |     25 | F      |                 50 | Calle Principal 153  |
|           98 | Juan Pérez Condori      | 73823960 | Paucartambo   | Paucartambo    |     34 | M      |                  6 | Urbanización Sol 414 |
|           99 | Ana Apaza Quispe        | 23597413 | Cusco         | Santiago       |     52 | M      |                 26 | Jr. Los Héroes 997   |
|          100 | Rosa Pérez Apaza        | 41621432 | Urubamba      | Urubamba       |     53 | F      |                 17 | Calle Principal 295  |
|          101 | Luis Pérez Quispe       | 22850052 | Quispicanchi  | Oropesa        |     73 | F      |                 48 | Av. Libertad 516     |
|          102 | María Apaza Pérez       | 56168594 | Urubamba      | Urubamba       |     74 | M      |                  4 | Calle Principal 337  |
|          103 | José Pérez Quispe       | 78980633 | Calca         | Pisac          |     23 | M      |                 14 | Calle Principal 81   |
|          104 | José Yupanqui Chávez    | 82360957 | La Convención | Quillabamba    |     72 | F      |                 45 | Pasaje Inca 361      |
|          105 | Lucía Huamán Huamán     | 88380857 | Quispicanchi  | Andahuaylillas |     32 | F      |                 18 | Pasaje Inca 290      |
|          106 | Rosa Huamán Mamani      | 45874074 | La Convención | Quillabamba    |     56 | F      |                 23 | Jr. Los Héroes 757   |
|          107 | Pedro Apaza Yupanqui    | 44759385 | Paucartambo   | Colquepata     |     85 | M      |                 38 | Av. Libertad 247     |
|          108 | Pedro Yupanqui Apaza    | 39539237 | Quispicanchi  | Oropesa        |     40 | M      |                  1 | Urbanización Sol 366 |
|          109 | María Quispe Pérez      | 85893932 | Urubamba      | Ollantaytambo  |     73 | M      |                 39 | Urbanización Sol 46  |
|          110 | José Yupanqui Yupanqui  | 38238837 | Calca         | Lamay          |     43 | M      |                 31 | Av. Libertad 431     |
|          111 | Carmen Apaza Huamán     | 50916080 | Canchis       | Checacupe      |     85 | M      |                 29 | Pasaje Inca 235      |
|          112 | Luis Quispe Chávez      | 40319301 | Urubamba      | Urubamba       |     57 | F      |                 28 | Pasaje Inca 388      |
|          113 | Lucía Huamán Yupanqui   | 59973324 | Urubamba      | Machu Picchu   |     62 | M      |                 39 | Jr. Los Héroes 732   |
|          114 | Luis Huamán Huamán      | 63215608 | Cusco         | San Jerónimo   |     77 | F      |                 10 | Urbanización Sol 810 |
|          115 | Rosa Flores Chávez      | 66668590 | Quispicanchi  | Oropesa        |     32 | M      |                  2 | Pasaje Inca 755      |
|          116 | Lucía Apaza Pérez       | 57824930 | La Convención | Echarate       |     66 | M      |                 31 | Urbanización Sol 552 |
|          117 | Luis Flores Pérez       | 45653687 | Urubamba      | Ollantaytambo  |     85 | F      |                 34 | Pasaje Inca 592      |
|          118 | José Condori Flores     | 89589353 | Quispicanchi  | Andahuaylillas |     68 | F      |                 30 | Jr. Los Héroes 945   |
|          119 | Rosa Quispe Ccopa       | 24732672 | La Convención | Echarate       |     52 | M      |                 26 | Urbanización Sol 500 |
|          120 | Luis Chávez Chávez      | 97409893 | La Convención | Quillabamba    |     84 | F      |                 19 | Calle Principal 801  |
|          121 | Juan Huamán Ccopa       | 64836281 | Quispicanchi  | Andahuaylillas |     28 | M      |                  7 | Pasaje Inca 545      |
|          122 | Pedro Flores Flores     | 35936241 | Quispicanchi  | Urcos          |     51 | F      |                  1 | Urbanización Sol 27  |
|          123 | José Ccopa Apaza        | 50344442 | Cusco         | San Sebastián  |     42 | F      |                 33 | Pasaje Inca 580      |
|          124 | Juan Yupanqui Mamani    | 60152762 | Calca         | Pisac          |     45 | F      |                 24 | Pasaje Inca 595      |
|          125 | Carmen Pérez Flores     | 94730109 | Canchis       | Sicuani        |     32 | F      |                 18 | Calle Principal 250  |
|          126 | María Huamán Mamani     | 52649246 | La Convención | Echarate       |     57 | M      |                 45 | Urbanización Sol 645 |
|          127 | Rosa Yupanqui Chávez    | 21131489 | Quispicanchi  | Urcos          |     44 | F      |                 16 | Pasaje Inca 594      |
|          128 | María Flores Yupanqui   | 97934164 | La Convención | Santa Teresa   |     22 | F      |                  6 | Calle Principal 152  |
|          129 | Pedro Flores Yupanqui   | 39997944 | Cusco         | San Jerónimo   |     71 | M      |                 10 | Pasaje Inca 403      |
|          130 | Rosa Condori Quispe     | 37202849 | Quispicanchi  | Urcos          |     83 | M      |                 50 | Urbanización Sol 488 |
|          131 | Miguel Flores Quispe    | 33741924 | La Convención | Echarate       |     28 | M      |                 18 | Urbanización Sol 535 |
|          132 | Juan Huamán Condori     | 16886069 | Canchis       | Sicuani        |     68 | M      |                 33 | Av. Libertad 994     |
|          133 | Rosa Quispe Pérez       | 22986534 | Calca         | Pisac          |     59 | F      |                  4 | Pasaje Inca 777      |
|          134 | María Apaza Apaza       | 63230895 | Cusco         | San Sebastián  |     46 | F      |                 46 | Av. Libertad 528     |
|          135 | Carmen Huamán Yupanqui  | 12277988 | Quispicanchi  | Andahuaylillas |     23 | F      |                 32 | Pasaje Inca 78       |
|          136 | Rosa Apaza Huamán       | 72665330 | Urubamba      | Ollantaytambo  |     82 | M      |                 25 | Jr. Los Héroes 162   |
|          137 | Pedro Condori Condori   | 81828136 | Calca         | Lamay          |     20 | F      |                  1 | Pasaje Inca 466      |
|          138 | María Ccopa Pérez       | 26454644 | Urubamba      | Machu Picchu   |     50 | F      |                 36 | Urbanización Sol 672 |
|          139 | Miguel Condori Apaza    | 49128416 | Canchis       | Sicuani        |     19 | M      |                 41 | Jr. Los Héroes 522   |
|          140 | Juan Yupanqui Quispe    | 40213405 | Cusco         | San Jerónimo   |     40 | M      |                 21 | Calle Principal 648  |
|          141 | Lucía Chávez Ccopa      | 16925559 | Canchis       | Checacupe      |     61 | M      |                 46 | Calle Principal 880  |
|          142 | Rosa Yupanqui Huamán    | 68651852 | Quispicanchi  | Andahuaylillas |     71 | M      |                 25 | Av. Libertad 954     |
|          143 | Luis Flores Condori     | 92616861 | Calca         | Lamay          |     55 | F      |                 15 | Calle Principal 86   |
|          144 | Pedro Flores Huamán     | 17797900 | La Convención | Santa Teresa   |     46 | M      |                 45 | Urbanización Sol 458 |
|          145 | Lucía Huamán Condori    | 84470337 | Quispicanchi  | Oropesa        |     75 | M      |                 28 | Jr. Los Héroes 289   |
|          146 | Ana Condori Apaza       | 17800111 | Urubamba      | Ollantaytambo  |     65 | F      |                  6 | Av. Libertad 874     |
|          147 | Juan Flores Ccopa       | 33694903 | Canchis       | Checacupe      |     37 | F      |                 26 | Av. Libertad 835     |
|          148 | Pedro Quispe Chávez     | 48257918 | Paucartambo   | Kosñipata      |     18 | M      |                 34 | Jr. Los Héroes 586   |
|          149 | Lucía Apaza Pérez       | 65599590 | Canchis       | San Pablo      |     38 | F      |                 23 | Urbanización Sol 483 |
|          150 | Pedro Apaza Quispe      | 86495598 | Quispicanchi  | Urcos          |     55 | M      |                 12 | Calle Principal 827  |
|          151 | Pedro Huamán Apaza      | 62962102 | Quispicanchi  | Andahuaylillas |     42 | M      |                  8 | Urbanización Sol 748 |
|          152 | Miguel Quispe Apaza     | 76761048 | Urubamba      | Urubamba       |     61 | M      |                 40 | Calle Principal 6    |
|          153 | Juan Huamán Pérez       | 84548026 | Urubamba      | Urubamba       |     18 | M      |                 43 | Pasaje Inca 901      |
|          154 | Juan Chávez Condori     | 30097898 | Quispicanchi  | Oropesa        |     41 | M      |                 28 | Calle Principal 510  |
|          155 | Lucía Huamán Huamán     | 11175179 | Urubamba      | Machu Picchu   |     47 | M      |                  6 | Pasaje Inca 291      |
|          156 | Luis Pérez Huamán       | 80104665 | Paucartambo   | Paucartambo    |     36 | M      |                 15 | Pasaje Inca 651      |
|          157 | Lucía Flores Quispe     | 29053843 | Calca         | Lamay          |     28 | F      |                  1 | Calle Principal 483  |
|          158 | Ana Flores Chávez       | 79432652 | Urubamba      | Urubamba       |     43 | M      |                 49 | Urbanización Sol 132 |
|          159 | Carmen Apaza Apaza      | 97769020 | Urubamba      | Ollantaytambo  |     84 | F      |                 48 | Calle Principal 292  |
|          160 | Lucía Yupanqui Yupanqui | 83379794 | Canchis       | Checacupe      |     29 | F      |                 40 | Calle Principal 552  |
|          161 | Juan Ccopa Huamán       | 25561066 | Quispicanchi  | Andahuaylillas |     20 | F      |                 40 | Calle Principal 590  |
|          162 | José Apaza Apaza        | 18735054 | Paucartambo   | Colquepata     |     47 | F      |                  1 | Av. Libertad 808     |
|          163 | Carmen Quispe Mamani    | 28483297 | Quispicanchi  | Andahuaylillas |     24 | M      |                 18 | Calle Principal 255  |
|          164 | José Yupanqui Apaza     | 36907378 | Calca         | Calca          |     73 | M      |                 49 | Urbanización Sol 473 |
|          165 | Carmen Pérez Mamani     | 18928080 | Calca         | Lamay          |     67 | F      |                 30 | Jr. Los Héroes 744   |
|          166 | Miguel Apaza Pérez      | 38251150 | Quispicanchi  | Urcos          |     72 | F      |                 34 | Av. Libertad 476     |
|          167 | Lucía Mamani Pérez      | 82977668 | Calca         | Calca          |     40 | M      |                 11 | Jr. Los Héroes 99    |
|          168 | Miguel Ccopa Pérez      | 98083631 | Canchis       | Checacupe      |     27 | M      |                 39 | Av. Libertad 271     |
|          169 | José Yupanqui Mamani    | 82220503 | Calca         | Calca          |     79 | F      |                 32 | Av. Libertad 739     |
|          170 | José Huamán Ccopa       | 22138436 | La Convención | Echarate       |     44 | M      |                 34 | Av. Libertad 301     |
|          171 | Ana Condori Yupanqui    | 14347322 | Cusco         | Wanchaq        |     75 | M      |                 10 | Calle Principal 354  |
|          172 | Ana Chávez Mamani       | 22006266 | La Convención | Quillabamba    |     76 | F      |                 35 | Urbanización Sol 110 |
|          173 | Carmen Ccopa Flores     | 49420287 | Paucartambo   | Kosñipata      |     57 | F      |                 11 | Jr. Los Héroes 819   |
|          174 | Rosa Quispe Ccopa       | 49043878 | Calca         | Lamay          |     28 | M      |                 18 | Jr. Los Héroes 601   |
|          175 | Miguel Ccopa Chávez     | 40627255 | Calca         | Lamay          |     28 | F      |                 14 | Jr. Los Héroes 435   |
|          176 | Juan Ccopa Flores       | 56233651 | Canchis       | San Pablo      |     22 | M      |                 13 | Jr. Los Héroes 448   |
|          177 | Rosa Mamani Pérez       | 79796226 | Paucartambo   | Paucartambo    |     32 | M      |                 32 | Calle Principal 854  |
|          178 | Rosa Flores Huamán      | 94427209 | Canchis       | Checacupe      |     31 | F      |                  1 | Pasaje Inca 455      |
|          179 | Miguel Mamani Yupanqui  | 10745922 | La Convención | Echarate       |     39 | F      |                 41 | Av. Libertad 156     |
|          180 | Miguel Apaza Condori    | 69282999 | La Convención | Quillabamba    |     34 | F      |                 42 | Jr. Los Héroes 503   |
|          181 | Lucía Huamán Pérez      | 17815720 | Canchis       | Sicuani        |     46 | M      |                 15 | Pasaje Inca 960      |
|          182 | Miguel Yupanqui Chávez  | 14816530 | Cusco         | San Sebastián  |     70 | M      |                 30 | Calle Principal 686  |
|          183 | Juan Yupanqui Mamani    | 64297827 | Calca         | Pisac          |     22 | F      |                 19 | Urbanización Sol 207 |
|          184 | María Huamán Yupanqui   | 64561728 | Quispicanchi  | Urcos          |     32 | M      |                 43 | Urbanización Sol 598 |
|          185 | Rosa Huamán Mamani      | 91872526 | Calca         | Pisac          |     75 | M      |                 33 | Calle Principal 205  |
|          186 | Luis Condori Chávez     | 53631529 | Calca         | Lamay          |     38 | M      |                 42 | Urbanización Sol 301 |
|          187 | María Quispe Yupanqui   | 17654288 | Quispicanchi  | Urcos          |     23 | M      |                 22 | Jr. Los Héroes 947   |
|          188 | Rosa Mamani Ccopa       | 61718666 | Quispicanchi  | Andahuaylillas |     35 | F      |                 39 | Jr. Los Héroes 242   |
|          189 | Ana Mamani Mamani       | 73873994 | Calca         | Lamay          |     71 | M      |                 31 | Urbanización Sol 189 |
|          190 | Luis Condori Mamani     | 62784579 | Cusco         | Wanchaq        |     20 | M      |                 19 | Jr. Los Héroes 243   |
|          191 | Miguel Huamán Mamani    | 49982486 | Cusco         | Wanchaq        |     64 | M      |                 35 | Av. Libertad 816     |
|          192 | Luis Chávez Ccopa       | 85281383 | Cusco         | Santiago       |     60 | M      |                 35 | Jr. Los Héroes 211   |
|          193 | María Pérez Condori     | 60903519 | Calca         | Lamay          |     61 | F      |                 37 | Calle Principal 769  |
|          194 | Carmen Condori Flores   | 71156676 | Urubamba      | Machu Picchu   |     28 | M      |                 43 | Calle Principal 866  |
|          195 | José Mamani Quispe      | 86543672 | Paucartambo   | Kosñipata      |     32 | M      |                 45 | Jr. Los Héroes 621   |
|          196 | Ana Apaza Chávez        | 42790613 | Canchis       | Sicuani        |     59 | M      |                 41 | Jr. Los Héroes 976   |
|          197 | Luis Quispe Yupanqui    | 10624276 | Calca         | Calca          |     38 | F      |                 16 | Jr. Los Héroes 259   |
|          198 | Juan Flores Apaza       | 60567346 | Quispicanchi  | Urcos          |     70 | F      |                 10 | Calle Principal 452  |
|          199 | Juan Mamani Ccopa       | 69365646 | Calca         | Lamay          |     57 | M      |                 11 | Jr. Los Héroes 682   |
|          200 | Pedro Pérez Mamani      | 58523974 | Canchis       | Sicuani        |     47 | F      |                 48 | Jr. Los Héroes 730   |
|          201 | Pedro Ccopa Condori     | 50064021 | Urubamba      | Ollantaytambo  |     72 | F      |                 48 | Jr. Los Héroes 533   |
|          202 | Pedro Flores Ccopa      | 94734059 | Quispicanchi  | Oropesa        |     71 | F      |                 13 | Pasaje Inca 325      |
|          203 | Rosa Pérez Quispe       | 44059279 | Urubamba      | Machu Picchu   |     22 | M      |                 18 | Av. Libertad 385     |
|          204 | Luis Flores Quispe      | 82846056 | La Convención | Santa Teresa   |     43 | M      |                 48 | Jr. Los Héroes 757   |
|          205 | Rosa Flores Yupanqui    | 25920365 | Quispicanchi  | Andahuaylillas |     47 | M      |                 41 | Jr. Los Héroes 591   |
|          206 | Ana Mamani Mamani       | 90335423 | Cusco         | San Jerónimo   |     23 | M      |                 30 | Pasaje Inca 999      |
|          207 | Luis Apaza Condori      | 53438085 | Quispicanchi  | Urcos          |     82 | F      |                 24 | Pasaje Inca 768      |
|          208 | Ana Condori Yupanqui    | 61326022 | Quispicanchi  | Urcos          |     54 | M      |                 49 | Calle Principal 282  |
|          209 | María Chávez Chávez     | 66618183 | Paucartambo   | Kosñipata      |     65 | M      |                 48 | Jr. Los Héroes 617   |
|          210 | Ana Yupanqui Ccopa      | 22207429 | Urubamba      | Machu Picchu   |     81 | M      |                 41 | Jr. Los Héroes 858   |
|          211 | María Condori Flores    | 40706009 | Canchis       | San Pablo      |     49 | M      |                 36 | Urbanización Sol 939 |
|          212 | Luis Flores Flores      | 92224647 | Canchis       | San Pablo      |     21 | M      |                  9 | Urbanización Sol 279 |
|          213 | Ana Yupanqui Chávez     | 70207038 | Cusco         | San Jerónimo   |     69 | F      |                 14 | Calle Principal 270  |
|          214 | Lucía Huamán Chávez     | 29541710 | Calca         | Calca          |     25 | F      |                 16 | Av. Libertad 775     |
|          215 | Miguel Huamán Ccopa     | 42116437 | Canchis       | San Pablo      |     78 | M      |                 10 | Jr. Los Héroes 157   |
|          216 | Rosa Ccopa Pérez        | 47599005 | Cusco         | Santiago       |     32 | M      |                 39 | Av. Libertad 852     |
|          217 | Miguel Quispe Chávez    | 17323265 | Canchis       | San Pablo      |     22 | M      |                  4 | Jr. Los Héroes 339   |
|          218 | Luis Yupanqui Ccopa     | 28380367 | Canchis       | Checacupe      |     67 | F      |                 21 | Jr. Los Héroes 239   |
|          219 | Lucía Condori Apaza     | 98305592 | Paucartambo   | Colquepata     |     61 | F      |                  1 | Pasaje Inca 486      |
|          220 | Carmen Quispe Chávez    | 18429376 | Paucartambo   | Kosñipata      |     21 | M      |                 21 | Pasaje Inca 223      |
|          221 | Miguel Yupanqui Condori | 62253442 | Quispicanchi  | Urcos          |     76 | F      |                  2 | Pasaje Inca 574      |
|          222 | Ana Mamani Condori      | 25252105 | Calca         | Calca          |     75 | M      |                 13 | Av. Libertad 959     |
|          223 | Lucía Mamani Condori    | 48832899 | Paucartambo   | Colquepata     |     84 | F      |                 12 | Pasaje Inca 312      |
|          224 | Juan Ccopa Apaza        | 65693601 | La Convención | Quillabamba    |     63 | F      |                 31 | Calle Principal 121  |
|          225 | Carmen Ccopa Chávez     | 71179876 | Urubamba      | Urubamba       |     34 | M      |                 11 | Jr. Los Héroes 684   |
|          226 | José Pérez Condori      | 88843628 | La Convención | Echarate       |     70 | F      |                 28 | Jr. Los Héroes 884   |
|          227 | Lucía Apaza Chávez      | 79714226 | Cusco         | San Jerónimo   |     59 | M      |                 22 | Av. Libertad 710     |
|          228 | Lucía Flores Ccopa      | 27111191 | Urubamba      | Urubamba       |     37 | M      |                 49 | Urbanización Sol 270 |
|          229 | Luis Huamán Ccopa       | 88081574 | Cusco         | San Sebastián  |     39 | F      |                  8 | Urbanización Sol 875 |
|          230 | Juan Chávez Flores      | 57941972 | Paucartambo   | Colquepata     |     56 | M      |                 31 | Calle Principal 269  |
|          231 | Lucía Quispe Chávez     | 24386124 | Cusco         | San Sebastián  |     50 | M      |                  7 | Urbanización Sol 403 |
|          232 | Luis Mamani Mamani      | 70799197 | Cusco         | San Jerónimo   |     70 | F      |                  9 | Pasaje Inca 558      |
|          233 | Pedro Condori Pérez     | 97385044 | Canchis       | San Pablo      |     64 | M      |                 37 | Pasaje Inca 893      |
|          234 | Luis Mamani Mamani      | 60207999 | Calca         | Pisac          |     54 | M      |                 24 | Pasaje Inca 39       |
|          235 | Ana Ccopa Mamani        | 74692134 | Quispicanchi  | Urcos          |     78 | F      |                 19 | Jr. Los Héroes 428   |
|          236 | Juan Pérez Quispe       | 24440497 | Calca         | Pisac          |     21 | M      |                 19 | Calle Principal 870  |
|          237 | Lucía Huamán Ccopa      | 61853355 | Cusco         | San Sebastián  |     70 | M      |                 36 | Calle Principal 852  |
|          238 | Carmen Apaza Apaza      | 84225376 | Urubamba      | Ollantaytambo  |     71 | M      |                  3 | Pasaje Inca 709      |
|          239 | Rosa Quispe Yupanqui    | 44554730 | Quispicanchi  | Andahuaylillas |     19 | M      |                 11 | Pasaje Inca 123      |
|          240 | Pedro Ccopa Condori     | 66476934 | Urubamba      | Ollantaytambo  |     63 | F      |                 36 | Pasaje Inca 775      |
|          241 | Rosa Ccopa Ccopa        | 45918462 | Quispicanchi  | Urcos          |     75 | F      |                 48 | Urbanización Sol 443 |
|          242 | Ana Ccopa Yupanqui      | 64548059 | Paucartambo   | Paucartambo    |     67 | F      |                 22 | Urbanización Sol 213 |
|          243 | Miguel Ccopa Condori    | 60647445 | Quispicanchi  | Urcos          |     27 | F      |                 10 | Av. Libertad 223     |
|          244 | José Apaza Mamani       | 86066830 | Urubamba      | Machu Picchu   |     74 | F      |                 31 | Calle Principal 730  |
|          245 | Miguel Yupanqui Pérez   | 22657216 | Quispicanchi  | Urcos          |     22 | M      |                 35 | Urbanización Sol 557 |
|          246 | Lucía Pérez Chávez      | 93360373 | Canchis       | San Pablo      |     84 | F      |                 40 | Urbanización Sol 366 |
|          247 | Carmen Apaza Ccopa      | 88222360 | Calca         | Pisac          |     49 | M      |                 31 | Calle Principal 297  |
|          248 | Luis Chávez Pérez       | 95890500 | Calca         | Pisac          |     41 | M      |                 34 | Calle Principal 706  |
|          249 | José Ccopa Mamani       | 80081158 | Cusco         | San Sebastián  |     67 | M      |                 16 | Urbanización Sol 510 |
|          250 | Juan Ccopa Condori      | 51390814 | Quispicanchi  | Oropesa        |     65 | F      |                 25 | Calle Principal 189  |
|          251 | Juan Mamani Chávez      | 85261451 | Urubamba      | Urubamba       |     49 | M      |                 35 | Jr. Los Héroes 592   |
|          252 | Luis Huamán Huamán      | 80965828 | La Convención | Santa Teresa   |     41 | F      |                 43 | Urbanización Sol 584 |
|          253 | María Pérez Pérez       | 19668259 | Canchis       | Sicuani        |     45 | F      |                 21 | Jr. Los Héroes 750   |
|          254 | Juan Apaza Pérez        | 32113855 | Canchis       | Checacupe      |     25 | F      |                  2 | Jr. Los Héroes 607   |
|          255 | Carmen Mamani Yupanqui  | 43770805 | Urubamba      | Ollantaytambo  |     44 | F      |                 39 | Calle Principal 454  |
|          256 | María Pérez Mamani      | 93470435 | Urubamba      | Ollantaytambo  |     75 | F      |                  4 | Calle Principal 901  |
|          257 | Pedro Pérez Apaza       | 15034153 | La Convención | Quillabamba    |     70 | M      |                  6 | Calle Principal 221  |
|          258 | Luis Pérez Apaza        | 84184386 | Canchis       | San Pablo      |     73 | M      |                 16 | Av. Libertad 494     |
|          259 | María Pérez Flores      | 85875351 | Paucartambo   | Kosñipata      |     55 | M      |                 46 | Jr. Los Héroes 949   |
|          260 | Ana Apaza Pérez         | 94875099 | Paucartambo   | Colquepata     |     79 | F      |                 45 | Pasaje Inca 925      |
|          261 | Miguel Quispe Apaza     | 38458035 | Paucartambo   | Colquepata     |     69 | F      |                 24 | Calle Principal 896  |
|          262 | José Ccopa Quispe       | 87840474 | La Convención | Quillabamba    |     68 | F      |                 40 | Urbanización Sol 40  |
|          263 | Pedro Huamán Pérez      | 93401319 | Calca         | Pisac          |     44 | M      |                 34 | Pasaje Inca 79       |
|          264 | María Flores Condori    | 89769812 | Calca         | Pisac          |     35 | M      |                 37 | Calle Principal 125  |
|          265 | José Chávez Yupanqui    | 78155842 | Quispicanchi  | Urcos          |     46 | F      |                  3 | Jr. Los Héroes 60    |
|          266 | Pedro Mamani Ccopa      | 60975976 | Cusco         | Santiago       |     45 | M      |                 31 | Pasaje Inca 654      |
|          267 | Ana Quispe Yupanqui     | 91049204 | Paucartambo   | Kosñipata      |     45 | M      |                 23 | Urbanización Sol 116 |
|          268 | Carmen Condori Huamán   | 53547836 | Cusco         | San Jerónimo   |     27 | F      |                  9 | Av. Libertad 709     |
|          269 | Carmen Yupanqui Chávez  | 51956750 | Urubamba      | Urubamba       |     52 | M      |                 35 | Av. Libertad 600     |
|          270 | Carmen Ccopa Quispe     | 40428431 | Canchis       | San Pablo      |     45 | M      |                  4 | Pasaje Inca 72       |
|          271 | Lucía Pérez Pérez       | 34204037 | Paucartambo   | Kosñipata      |     43 | M      |                 42 | Jr. Los Héroes 44    |
|          272 | Luis Yupanqui Flores    | 28957027 | Cusco         | Wanchaq        |     69 | F      |                  9 | Calle Principal 919  |
|          273 | Carmen Condori Mamani   | 67262260 | Canchis       | Sicuani        |     52 | M      |                  7 | Urbanización Sol 258 |
|          274 | Juan Quispe Chávez      | 72723068 | Paucartambo   | Colquepata     |     58 | F      |                 18 | Jr. Los Héroes 322   |
|          275 | María Ccopa Huamán      | 10277524 | La Convención | Santa Teresa   |     29 | M      |                 27 | Jr. Los Héroes 843   |
|          276 | Luis Ccopa Chávez       | 97566458 | Canchis       | Checacupe      |     45 | M      |                 19 | Av. Libertad 532     |
|          277 | José Mamani Ccopa       | 19550116 | Calca         | Calca          |     38 | M      |                  2 | Jr. Los Héroes 491   |
|          278 | Luis Ccopa Mamani       | 86032278 | Canchis       | San Pablo      |     34 | F      |                 35 | Av. Libertad 175     |
|          279 | Luis Quispe Apaza       | 15511424 | Paucartambo   | Paucartambo    |     44 | F      |                 39 | Jr. Los Héroes 416   |
|          280 | Juan Chávez Quispe      | 51118204 | Urubamba      | Machu Picchu   |     81 | M      |                 39 | Av. Libertad 940     |
|          281 | Luis Ccopa Quispe       | 95244593 | Paucartambo   | Paucartambo    |     66 | F      |                 46 | Calle Principal 669  |
|          282 | Pedro Quispe Quispe     | 36972889 | Canchis       | San Pablo      |     27 | M      |                 44 | Av. Libertad 442     |
|          283 | Lucía Flores Yupanqui   | 24682539 | Cusco         | Wanchaq        |     37 | M      |                  2 | Calle Principal 657  |
|          284 | María Apaza Huamán      | 73249403 | Urubamba      | Ollantaytambo  |     30 | F      |                 14 | Calle Principal 368  |
|          285 | Pedro Ccopa Yupanqui    | 15916784 | La Convención | Echarate       |     39 | F      |                  4 | Av. Libertad 784     |
|          286 | María Pérez Quispe      | 30618323 | Cusco         | San Sebastián  |     69 | F      |                 44 | Pasaje Inca 98       |
|          287 | Ana Apaza Pérez         | 62629949 | Cusco         | San Sebastián  |     75 | F      |                 14 | Calle Principal 125  |
|          288 | Rosa Apaza Condori      | 35915282 | Calca         | Lamay          |     25 | M      |                 32 | Urbanización Sol 850 |
|          289 | Lucía Quispe Condori    | 35891907 | Canchis       | Checacupe      |     47 | F      |                 28 | Calle Principal 28   |
|          290 | Lucía Pérez Ccopa       | 67993532 | Calca         | Calca          |     72 | F      |                 28 | Av. Libertad 642     |
|          291 | Lucía Pérez Apaza       | 75003020 | Urubamba      | Urubamba       |     70 | M      |                 41 | Calle Principal 658  |
|          292 | María Condori Condori   | 16003307 | Paucartambo   | Paucartambo    |     42 | M      |                 40 | Jr. Los Héroes 712   |
|          293 | Pedro Yupanqui Condori  | 19217669 | Paucartambo   | Colquepata     |     41 | F      |                 27 | Calle Principal 155  |
|          294 | Lucía Chávez Ccopa      | 51781123 | Quispicanchi  | Urcos          |     18 | M      |                  6 | Av. Libertad 838     |
|          295 | José Ccopa Yupanqui     | 95379750 | Cusco         | San Jerónimo   |     60 | F      |                 27 | Av. Libertad 322     |
|          296 | Carmen Flores Ccopa     | 92613387 | Paucartambo   | Kosñipata      |     56 | F      |                 12 | Calle Principal 286  |
|          297 | María Huamán Quispe     | 55489445 | Paucartambo   | Colquepata     |     43 | F      |                 22 | Pasaje Inca 558      |
|          298 | Miguel Yupanqui Condori | 24424827 | Urubamba      | Machu Picchu   |     60 | F      |                 42 | Jr. Los Héroes 446   |
|          299 | Miguel Condori Pérez    | 51432373 | Urubamba      | Urubamba       |     79 | F      |                  8 | Pasaje Inca 151      |
|          300 | Miguel Mamani Mamani    | 49347106 | Canchis       | Checacupe      |     71 | F      |                 19 | Urbanización Sol 175 |
|          301 | Juan Yupanqui Quispe    | 92899587 | Calca         | Lamay          |     41 | M      |                  5 | Jr. Los Héroes 341   |
|          302 | María Ccopa Flores      | 69990264 | Paucartambo   | Colquepata     |     85 | M      |                 26 | Av. Libertad 410     |
|          303 | Ana Quispe Flores       | 24628734 | Canchis       | Checacupe      |     74 | M      |                 24 | Pasaje Inca 360      |
|          304 | María Chávez Yupanqui   | 93532953 | La Convención | Quillabamba    |     31 | M      |                 10 | Urbanización Sol 834 |
|          305 | Luis Yupanqui Mamani    | 10181150 | Calca         | Calca          |     26 | F      |                 16 | Pasaje Inca 391      |
|          306 | Luis Huamán Mamani      | 69001364 | Canchis       | Sicuani        |     42 | M      |                  7 | Pasaje Inca 54       |
|          307 | Carmen Flores Condori   | 61341168 | Calca         | Lamay          |     38 | F      |                 30 | Urbanización Sol 116 |
|          308 | Pedro Apaza Ccopa       | 92851022 | Cusco         | San Jerónimo   |     33 | M      |                 33 | Pasaje Inca 974      |
|          309 | Ana Huamán Huamán       | 63990620 | La Convención | Echarate       |     85 | M      |                  5 | Pasaje Inca 123      |
|          310 | Lucía Apaza Apaza       | 34120365 | Quispicanchi  | Oropesa        |     69 | F      |                 27 | Urbanización Sol 318 |
|          311 | Ana Apaza Yupanqui      | 25569662 | Quispicanchi  | Andahuaylillas |     70 | F      |                 50 | Calle Principal 516  |
|          312 | Miguel Quispe Chávez    | 70206767 | Canchis       | San Pablo      |     40 | M      |                 42 | Pasaje Inca 487      |
|          313 | Carmen Yupanqui Huamán  | 76870364 | Canchis       | Sicuani        |     30 | F      |                 30 | Jr. Los Héroes 554   |
|          314 | Luis Condori Chávez     | 27446024 | Cusco         | Wanchaq        |     20 | F      |                 38 | Av. Libertad 982     |
|          315 | María Apaza Quispe      | 89117322 | La Convención | Echarate       |     20 | F      |                  6 | Calle Principal 961  |
|          316 | Rosa Mamani Huamán      | 46696442 | Paucartambo   | Colquepata     |     71 | M      |                 17 | Urbanización Sol 764 |
|          317 | Rosa Pérez Yupanqui     | 48236005 | Calca         | Lamay          |     73 | F      |                 19 | Pasaje Inca 600      |
|          318 | Luis Flores Pérez       | 43076546 | Urubamba      | Ollantaytambo  |     62 | M      |                 30 | Calle Principal 327  |
|          319 | José Condori Huamán     | 67275973 | Canchis       | Sicuani        |     25 | M      |                 22 | Urbanización Sol 276 |
|          320 | Miguel Yupanqui Quispe  | 93141698 | Quispicanchi  | Andahuaylillas |     42 | F      |                 42 | Av. Libertad 604     |
|          321 | Lucía Quispe Huamán     | 88326222 | La Convención | Quillabamba    |     28 | M      |                 40 | Jr. Los Héroes 400   |
|          322 | Ana Pérez Condori       | 75557851 | Paucartambo   | Kosñipata      |     70 | M      |                  2 | Av. Libertad 764     |
|          323 | Luis Yupanqui Quispe    | 44534511 | Quispicanchi  | Urcos          |     47 | F      |                 45 | Av. Libertad 205     |
|          324 | Luis Huamán Yupanqui    | 44557517 | Cusco         | Wanchaq        |     79 | F      |                 34 | Av. Libertad 389     |
|          325 | Ana Mamani Condori      | 37628869 | Calca         | Pisac          |     68 | F      |                  1 | Calle Principal 349  |
|          326 | Carmen Ccopa Chávez     | 58852221 | Quispicanchi  | Urcos          |     28 | F      |                 35 | Jr. Los Héroes 721   |
|          327 | Miguel Ccopa Yupanqui   | 37332543 | Calca         | Calca          |     44 | F      |                 48 | Pasaje Inca 697      |
|          328 | Carmen Chávez Pérez     | 31880864 | Cusco         | Santiago       |     80 | F      |                 11 | Av. Libertad 246     |
|          329 | Juan Condori Apaza      | 95184348 | Paucartambo   | Paucartambo    |     66 | F      |                 18 | Urbanización Sol 781 |
|          330 | Carmen Chávez Pérez     | 64793381 | La Convención | Quillabamba    |     18 | M      |                  8 | Jr. Los Héroes 271   |
|          331 | Lucía Apaza Yupanqui    | 56361518 | Calca         | Calca          |     18 | F      |                  6 | Av. Libertad 897     |
|          332 | Rosa Yupanqui Quispe    | 23090881 | Urubamba      | Urubamba       |     59 | F      |                 13 | Urbanización Sol 708 |
|          333 | José Condori Mamani     | 56013730 | Urubamba      | Ollantaytambo  |     75 | F      |                 19 | Calle Principal 751  |
|          334 | María Flores Ccopa      | 70025076 | Urubamba      | Machu Picchu   |     34 | M      |                 43 | Pasaje Inca 856      |
|          335 | Rosa Chávez Yupanqui    | 84135561 | La Convención | Quillabamba    |     77 | M      |                 23 | Calle Principal 715  |
|          336 | Juan Flores Apaza       | 70004433 | La Convención | Santa Teresa   |     79 | M      |                 33 | Jr. Los Héroes 626   |
|          337 | Juan Condori Chávez     | 87855968 | Urubamba      | Urubamba       |     41 | M      |                 40 | Jr. Los Héroes 404   |
|          338 | María Chávez Huamán     | 72632194 | Calca         | Calca          |     29 | F      |                 23 | Calle Principal 162  |
|          339 | José Yupanqui Apaza     | 38054902 | Urubamba      | Ollantaytambo  |     27 | F      |                  3 | Calle Principal 634  |
|          340 | Carmen Chávez Pérez     | 84255221 | Calca         | Pisac          |     82 | F      |                 14 | Jr. Los Héroes 244   |
|          341 | Juan Condori Pérez      | 17656993 | Calca         | Calca          |     43 | M      |                  6 | Pasaje Inca 441      |
|          342 | Rosa Quispe Huamán      | 25669974 | Quispicanchi  | Urcos          |     32 | F      |                  8 | Av. Libertad 567     |
|          343 | José Condori Condori    | 43117987 | Canchis       | San Pablo      |     70 | F      |                 40 | Jr. Los Héroes 826   |
|          344 | Luis Flores Huamán      | 99564800 | Canchis       | San Pablo      |     70 | F      |                 43 | Calle Principal 518  |
|          345 | Rosa Apaza Flores       | 30579549 | Urubamba      | Urubamba       |     47 | F      |                 22 | Jr. Los Héroes 295   |
|          346 | Carmen Flores Condori   | 69556610 | La Convención | Echarate       |     56 | M      |                 34 | Av. Libertad 898     |
|          347 | Rosa Pérez Pérez        | 14989268 | Canchis       | Checacupe      |     77 | F      |                 35 | Av. Libertad 959     |
|          348 | José Quispe Ccopa       | 15941586 | Calca         | Lamay          |     27 | F      |                 25 | Av. Libertad 4       |
|          349 | Pedro Flores Ccopa      | 56575555 | Quispicanchi  | Oropesa        |     81 | F      |                 47 | Av. Libertad 887     |
|          350 | Luis Quispe Apaza       | 36062107 | Urubamba      | Urubamba       |     59 | F      |                 17 | Av. Libertad 233     |
|          351 | Pedro Chávez Flores     | 53798208 | Quispicanchi  | Andahuaylillas |     23 | M      |                  2 | Jr. Los Héroes 294   |
|          352 | Pedro Pérez Condori     | 94303901 | La Convención | Quillabamba    |     45 | F      |                 17 | Calle Principal 393  |
|          353 | Miguel Huamán Chávez    | 42213454 | Quispicanchi  | Oropesa        |     65 | M      |                 25 | Jr. Los Héroes 575   |
|          354 | Lucía Huamán Huamán     | 58197524 | Calca         | Lamay          |     74 | F      |                 28 | Urbanización Sol 402 |
|          355 | María Pérez Condori     | 86322019 | La Convención | Quillabamba    |     26 | M      |                  9 | Av. Libertad 501     |
|          356 | Juan Pérez Pérez        | 58382971 | Quispicanchi  | Andahuaylillas |     20 | F      |                 18 | Calle Principal 104  |
|          357 | Ana Huamán Pérez        | 29020623 | Canchis       | Checacupe      |     53 | F      |                 29 | Urbanización Sol 589 |
|          358 | Miguel Quispe Condori   | 84848583 | Quispicanchi  | Oropesa        |     63 | F      |                 32 | Av. Libertad 920     |
|          359 | Ana Huamán Pérez        | 70124266 | Cusco         | San Sebastián  |     71 | F      |                 34 | Av. Libertad 752     |
|          360 | María Condori Quispe    | 96501550 | Quispicanchi  | Urcos          |     30 | M      |                 29 | Av. Libertad 796     |
|          361 | Lucía Condori Chávez    | 32284770 | Quispicanchi  | Urcos          |     83 | F      |                 43 | Calle Principal 195  |
|          362 | Pedro Quispe Apaza      | 10650628 | Urubamba      | Ollantaytambo  |     53 | M      |                  1 | Av. Libertad 808     |
|          363 | José Yupanqui Mamani    | 28755907 | Calca         | Lamay          |     26 | M      |                  6 | Av. Libertad 758     |
|          364 | María Yupanqui Quispe   | 83071306 | Canchis       | Sicuani        |     66 | F      |                 21 | Calle Principal 740  |
|          365 | Lucía Condori Chávez    | 12052293 | Canchis       | Sicuani        |     41 | F      |                 37 | Pasaje Inca 468      |
|          366 | Juan Ccopa Mamani       | 28483533 | Cusco         | San Jerónimo   |     80 | M      |                 32 | Calle Principal 247  |
|          367 | Luis Huamán Condori     | 68994642 | Cusco         | Wanchaq        |     57 | F      |                 25 | Jr. Los Héroes 703   |
|          368 | Carmen Flores Mamani    | 90912571 | Urubamba      | Ollantaytambo  |     56 | F      |                 15 | Jr. Los Héroes 413   |
|          369 | Lucía Yupanqui Apaza    | 21208888 | Calca         | Lamay          |     61 | M      |                  3 | Av. Libertad 186     |
|          370 | José Quispe Mamani      | 42216459 | Urubamba      | Urubamba       |     23 | M      |                 44 | Calle Principal 983  |
|          371 | Pedro Pérez Mamani      | 92070212 | Paucartambo   | Paucartambo    |     74 | M      |                 18 | Av. Libertad 288     |
|          372 | Lucía Apaza Pérez       | 24367334 | Cusco         | San Jerónimo   |     64 | F      |                 46 | Urbanización Sol 393 |
|          373 | Lucía Flores Mamani     | 36955714 | Cusco         | San Sebastián  |     74 | F      |                 44 | Urbanización Sol 226 |
|          374 | José Ccopa Huamán       | 96096045 | Cusco         | Wanchaq        |     60 | F      |                 40 | Calle Principal 861  |
|          375 | Carmen Chávez Pérez     | 83283240 | Quispicanchi  | Oropesa        |     45 | F      |                 30 | Urbanización Sol 213 |
|          376 | Carmen Condori Pérez    | 85366674 | Urubamba      | Ollantaytambo  |     37 | F      |                  9 | Urbanización Sol 597 |
|          377 | Lucía Apaza Yupanqui    | 51733110 | Urubamba      | Ollantaytambo  |     63 | M      |                 50 | Pasaje Inca 935      |
|          378 | Luis Quispe Chávez      | 53170556 | Paucartambo   | Colquepata     |     76 | F      |                 14 | Pasaje Inca 335      |
|          379 | Carmen Pérez Mamani     | 52537280 | La Convención | Santa Teresa   |     51 | F      |                 23 | Jr. Los Héroes 251   |
|          380 | Rosa Flores Apaza       | 77497273 | Canchis       | Checacupe      |     26 | M      |                 28 | Av. Libertad 116     |
|          381 | Pedro Pérez Pérez       | 18749380 | Calca         | Pisac          |     34 | M      |                 17 | Calle Principal 893  |
|          382 | Pedro Apaza Ccopa       | 96031357 | Urubamba      | Machu Picchu   |     53 | M      |                 49 | Av. Libertad 319     |
|          383 | Lucía Apaza Pérez       | 23511554 | Cusco         | Wanchaq        |     62 | F      |                 38 | Pasaje Inca 982      |
|          384 | María Apaza Yupanqui    | 77655703 | Quispicanchi  | Oropesa        |     40 | M      |                  7 | Av. Libertad 879     |
|          385 | Luis Ccopa Condori      | 31365235 | Cusco         | San Jerónimo   |     48 | F      |                 44 | Pasaje Inca 155      |
|          386 | Ana Condori Yupanqui    | 82397383 | Canchis       | Sicuani        |     77 | F      |                 22 | Urbanización Sol 139 |
|          387 | Juan Ccopa Chávez       | 11735564 | Urubamba      | Ollantaytambo  |     41 | M      |                 15 | Urbanización Sol 75  |
|          388 | María Mamani Pérez      | 94504166 | Calca         | Pisac          |     63 | F      |                  3 | Av. Libertad 372     |
|          389 | Carmen Yupanqui Flores  | 12315016 | Quispicanchi  | Andahuaylillas |     65 | M      |                 21 | Urbanización Sol 202 |
|          390 | Miguel Flores Chávez    | 91728000 | Urubamba      | Urubamba       |     84 | M      |                 50 | Pasaje Inca 766      |
|          391 | Miguel Pérez Quispe     | 72802611 | Urubamba      | Ollantaytambo  |     57 | M      |                  2 | Jr. Los Héroes 9     |
|          392 | Juan Quispe Apaza       | 42298353 | Urubamba      | Urubamba       |     76 | F      |                 32 | Calle Principal 926  |
|          393 | Luis Ccopa Quispe       | 76972143 | Cusco         | San Jerónimo   |     43 | M      |                 34 | Urbanización Sol 94  |
|          394 | Pedro Yupanqui Ccopa    | 53044516 | Urubamba      | Urubamba       |     36 | F      |                 10 | Urbanización Sol 936 |
|          395 | Pedro Mamani Condori    | 44147000 | Canchis       | San Pablo      |     35 | F      |                 49 | Av. Libertad 638     |
|          396 | Lucía Apaza Condori     | 71285184 | Urubamba      | Ollantaytambo  |     77 | M      |                 20 | Calle Principal 353  |
|          397 | Luis Chávez Mamani      | 10577421 | Canchis       | Checacupe      |     63 | F      |                 10 | Calle Principal 945  |
|          398 | Carmen Huamán Condori   | 50375840 | Urubamba      | Urubamba       |     58 | F      |                 31 | Jr. Los Héroes 974   |
|          399 | Juan Huamán Condori     | 83165497 | La Convención | Quillabamba    |     71 | M      |                 36 | Calle Principal 851  |
|          400 | José Mamani Ccopa       | 17617212 | Cusco         | Wanchaq        |     71 | F      |                  4 | Av. Libertad 733     |
|          401 | María Quispe Apaza      | 42586249 | Canchis       | San Pablo      |     60 | F      |                 23 | Av. Libertad 485     |
|          402 | Rosa Pérez Apaza        | 10737128 | La Convención | Santa Teresa   |     63 | M      |                 43 | Av. Libertad 430     |
|          403 | Juan Condori Pérez      | 66194817 | Quispicanchi  | Andahuaylillas |     57 | F      |                 11 | Urbanización Sol 4   |
|          404 | Lucía Condori Condori   | 87288994 | Calca         | Calca          |     28 | F      |                 36 | Av. Libertad 608     |
|          405 | Rosa Huamán Apaza       | 29504527 | Cusco         | Wanchaq        |     75 | F      |                 42 | Av. Libertad 489     |
|          406 | Carmen Condori Yupanqui | 74707580 | Urubamba      | Ollantaytambo  |     79 | F      |                 23 | Jr. Los Héroes 40    |
|          407 | Pedro Pérez Flores      | 94673911 | Quispicanchi  | Andahuaylillas |     31 | F      |                 25 | Av. Libertad 859     |
|          408 | Pedro Flores Huamán     | 98132028 | Quispicanchi  | Urcos          |     81 | F      |                 20 | Calle Principal 996  |
|          409 | Pedro Huamán Condori    | 31751509 | Calca         | Pisac          |     26 | F      |                 50 | Av. Libertad 564     |
|          410 | Rosa Huamán Huamán      | 40999549 | Paucartambo   | Paucartambo    |     76 | M      |                 30 | Jr. Los Héroes 766   |
|          411 | Ana Flores Quispe       | 38522489 | Cusco         | Wanchaq        |     34 | M      |                 35 | Calle Principal 925  |
|          412 | Pedro Apaza Quispe      | 19176931 | Cusco         | Wanchaq        |     37 | M      |                 21 | Calle Principal 979  |
|          413 | José Apaza Pérez        | 59010870 | Cusco         | Santiago       |     37 | F      |                  8 | Urbanización Sol 800 |
|          414 | Pedro Pérez Condori     | 37143600 | Urubamba      | Machu Picchu   |     45 | F      |                 28 | Calle Principal 367  |
|          415 | Pedro Chávez Yupanqui   | 24056755 | Urubamba      | Machu Picchu   |     25 | F      |                 48 | Jr. Los Héroes 836   |
|          416 | Lucía Ccopa Mamani      | 79416121 | Cusco         | Wanchaq        |     55 | M      |                 17 | Pasaje Inca 938      |
|          417 | Lucía Flores Apaza      | 37503656 | Paucartambo   | Paucartambo    |     74 | F      |                 18 | Av. Libertad 172     |
|          418 | Pedro Quispe Quispe     | 14621131 | Cusco         | San Jerónimo   |     67 | F      |                 24 | Av. Libertad 445     |
|          419 | Pedro Ccopa Yupanqui    | 90372129 | Calca         | Lamay          |     52 | M      |                 39 | Jr. Los Héroes 789   |
|          420 | Lucía Chávez Mamani     | 85091770 | Canchis       | Checacupe      |     45 | F      |                 23 | Av. Libertad 520     |
|          421 | Carmen Condori Huamán   | 93031530 | Canchis       | Sicuani        |     71 | M      |                 47 | Av. Libertad 527     |
|          422 | Pedro Mamani Condori    | 42850218 | Quispicanchi  | Oropesa        |     30 | M      |                 37 | Pasaje Inca 274      |
|          423 | María Yupanqui Ccopa    | 36949464 | Canchis       | San Pablo      |     36 | M      |                 36 | Pasaje Inca 6        |
|          424 | Juan Pérez Huamán       | 47269484 | Quispicanchi  | Urcos          |     83 | M      |                 49 | Av. Libertad 47      |
|          425 | Rosa Pérez Pérez        | 86535670 | Canchis       | Checacupe      |     52 | F      |                 31 | Jr. Los Héroes 424   |
|          426 | Carmen Yupanqui Huamán  | 65336599 | Canchis       | San Pablo      |     56 | F      |                 46 | Jr. Los Héroes 103   |
|          427 | José Quispe Chávez      | 77430260 | Calca         | Pisac          |     69 | M      |                 14 | Jr. Los Héroes 830   |
|          428 | Miguel Flores Apaza     | 82570307 | Paucartambo   | Paucartambo    |     73 | F      |                  6 | Calle Principal 246  |
|          429 | María Apaza Huamán      | 43735721 | La Convención | Echarate       |     26 | F      |                 46 | Pasaje Inca 346      |
|          430 | Carmen Chávez Quispe    | 16796126 | Quispicanchi  | Urcos          |     26 | M      |                 41 | Av. Libertad 502     |
|          431 | Rosa Quispe Mamani      | 36569228 | Calca         | Calca          |     26 | M      |                 29 | Pasaje Inca 394      |
|          432 | Lucía Pérez Quispe      | 85559871 | Urubamba      | Urubamba       |     69 | F      |                 46 | Calle Principal 354  |
|          433 | Juan Chávez Pérez       | 39454207 | Calca         | Calca          |     58 | F      |                 21 | Pasaje Inca 433      |
|          434 | Rosa Ccopa Ccopa        | 58320650 | Paucartambo   | Colquepata     |     82 | M      |                 38 | Pasaje Inca 548      |
|          435 | Rosa Huamán Quispe      | 23149504 | Paucartambo   | Paucartambo    |     56 | F      |                 18 | Pasaje Inca 414      |
|          436 | Luis Mamani Flores      | 51500255 | Urubamba      | Urubamba       |     76 | M      |                 40 | Pasaje Inca 818      |
|          437 | Carmen Huamán Ccopa     | 92623724 | Urubamba      | Machu Picchu   |     37 | M      |                  9 | Calle Principal 739  |
|          438 | Rosa Huamán Huamán      | 35671940 | Cusco         | San Jerónimo   |     46 | M      |                 48 | Av. Libertad 961     |
|          439 | Lucía Chávez Huamán     | 81328509 | La Convención | Echarate       |     33 | M      |                  3 | Pasaje Inca 296      |
|          440 | José Yupanqui Condori   | 97604464 | Paucartambo   | Paucartambo    |     55 | F      |                 26 | Jr. Los Héroes 442   |
|          441 | Ana Quispe Chávez       | 51763771 | Cusco         | San Sebastián  |     47 | F      |                 39 | Calle Principal 455  |
|          442 | Lucía Pérez Pérez       | 17135165 | Urubamba      | Ollantaytambo  |     65 | M      |                 26 | Urbanización Sol 110 |
|          443 | Luis Chávez Ccopa       | 12789849 | La Convención | Santa Teresa   |     77 | M      |                 27 | Av. Libertad 338     |
|          444 | Juan Ccopa Ccopa        | 48045259 | Cusco         | San Sebastián  |     19 | F      |                 42 | Urbanización Sol 264 |
|          445 | Rosa Pérez Flores       | 28859609 | Cusco         | Santiago       |     25 | F      |                 17 | Jr. Los Héroes 482   |
|          446 | Miguel Flores Mamani    | 75569437 | Paucartambo   | Kosñipata      |     20 | F      |                 33 | Urbanización Sol 364 |
|          447 | Luis Condori Yupanqui   | 45800358 | Cusco         | San Sebastián  |     75 | F      |                 43 | Pasaje Inca 223      |
|          448 | Ana Quispe Yupanqui     | 86552658 | Paucartambo   | Paucartambo    |     20 | F      |                 13 | Urbanización Sol 677 |
|          449 | José Pérez Quispe       | 42980583 | Cusco         | Santiago       |     76 | F      |                 31 | Urbanización Sol 482 |
|          450 | Pedro Flores Quispe     | 48597107 | Canchis       | San Pablo      |     42 | F      |                  7 | Pasaje Inca 375      |
|          451 | Lucía Pérez Ccopa       | 75952008 | La Convención | Echarate       |     52 | M      |                  2 | Jr. Los Héroes 944   |
|          452 | Luis Mamani Apaza       | 75156513 | Paucartambo   | Kosñipata      |     31 | M      |                 12 | Calle Principal 752  |
|          453 | Juan Quispe Mamani      | 42415574 | La Convención | Quillabamba    |     33 | M      |                 43 | Av. Libertad 753     |
|          454 | Juan Huamán Chávez      | 85785764 | Urubamba      | Urubamba       |     72 | M      |                 36 | Jr. Los Héroes 667   |
|          455 | Lucía Chávez Pérez      | 74198937 | Paucartambo   | Paucartambo    |     71 | M      |                 18 | Pasaje Inca 805      |
|          456 | Ana Apaza Flores        | 81462735 | Quispicanchi  | Urcos          |     39 | F      |                 39 | Pasaje Inca 971      |
|          457 | Miguel Flores Apaza     | 34943287 | Canchis       | Sicuani        |     77 | M      |                 41 | Urbanización Sol 291 |
|          458 | Ana Yupanqui Mamani     | 35126017 | Cusco         | Santiago       |     25 | F      |                 16 | Jr. Los Héroes 594   |
|          459 | Rosa Mamani Yupanqui    | 99150612 | Cusco         | San Jerónimo   |     36 | F      |                 42 | Calle Principal 597  |
|          460 | Luis Mamani Chávez      | 75481541 | Urubamba      | Machu Picchu   |     37 | F      |                 45 | Jr. Los Héroes 688   |
|          461 | Ana Chávez Quispe       | 65321665 | Calca         | Lamay          |     48 | M      |                  8 | Urbanización Sol 605 |
|          462 | José Ccopa Flores       | 35312985 | Canchis       | San Pablo      |     19 | F      |                 46 | Pasaje Inca 297      |
|          463 | Carmen Condori Pérez    | 58465511 | Quispicanchi  | Urcos          |     75 | F      |                 33 | Pasaje Inca 564      |
|          464 | Rosa Ccopa Huamán       | 99412374 | Paucartambo   | Paucartambo    |     23 | M      |                 39 | Av. Libertad 362     |
|          465 | Miguel Chávez Condori   | 49251535 | Cusco         | San Jerónimo   |     36 | M      |                 30 | Urbanización Sol 435 |
|          466 | Ana Yupanqui Mamani     | 59249288 | Canchis       | Sicuani        |     48 | F      |                 43 | Jr. Los Héroes 853   |
|          467 | María Condori Apaza     | 76901357 | Canchis       | Checacupe      |     84 | M      |                 41 | Urbanización Sol 709 |
|          468 | Rosa Mamani Yupanqui    | 69495575 | Quispicanchi  | Oropesa        |     32 | M      |                  2 | Urbanización Sol 203 |
|          469 | Miguel Apaza Quispe     | 86116566 | Cusco         | Santiago       |     45 | M      |                  4 | Av. Libertad 823     |
|          470 | Pedro Ccopa Apaza       | 77322647 | Urubamba      | Machu Picchu   |     34 | F      |                 44 | Av. Libertad 674     |
|          471 | Rosa Mamani Flores      | 27202449 | Paucartambo   | Colquepata     |     32 | M      |                 12 | Pasaje Inca 541      |
|          472 | Pedro Condori Yupanqui  | 35612669 | Urubamba      | Urubamba       |     29 | F      |                 26 | Pasaje Inca 692      |
|          473 | Pedro Ccopa Yupanqui    | 48010218 | Canchis       | Sicuani        |     71 | F      |                  2 | Av. Libertad 339     |
|          474 | Carmen Ccopa Huamán     | 21032424 | Canchis       | San Pablo      |     58 | F      |                 29 | Urbanización Sol 521 |
|          475 | María Condori Chávez    | 20251561 | Calca         | Calca          |     27 | M      |                 28 | Av. Libertad 217     |
|          476 | Miguel Flores Ccopa     | 27167562 | Quispicanchi  | Andahuaylillas |     84 | M      |                 39 | Calle Principal 910  |
|          477 | Ana Pérez Condori       | 50933437 | Paucartambo   | Kosñipata      |     66 | M      |                  3 | Calle Principal 212  |
|          478 | Lucía Flores Huamán     | 60555679 | La Convención | Santa Teresa   |     28 | M      |                 19 | Urbanización Sol 740 |
|          479 | María Quispe Apaza      | 78529265 | Cusco         | Wanchaq        |     31 | M      |                 32 | Pasaje Inca 516      |
|          480 | Juan Ccopa Apaza        | 45285842 | Paucartambo   | Kosñipata      |     65 | M      |                 19 | Calle Principal 963  |
|          481 | Lucía Huamán Condori    | 14634435 | Canchis       | Sicuani        |     41 | F      |                 46 | Pasaje Inca 242      |
|          482 | Miguel Ccopa Apaza      | 57274351 | Urubamba      | Ollantaytambo  |     77 | M      |                 20 | Urbanización Sol 495 |
|          483 | Pedro Mamani Ccopa      | 93527229 | Urubamba      | Ollantaytambo  |     20 | F      |                 40 | Calle Principal 531  |
|          484 | Pedro Apaza Chávez      | 76803616 | Urubamba      | Ollantaytambo  |     58 | F      |                  8 | Urbanización Sol 615 |
|          485 | Juan Yupanqui Pérez     | 94527784 | Calca         | Lamay          |     48 | M      |                  9 | Jr. Los Héroes 388   |
|          486 | Juan Ccopa Ccopa        | 69025097 | Quispicanchi  | Oropesa        |     69 | F      |                 38 | Jr. Los Héroes 172   |
|          487 | Ana Apaza Chávez        | 46834095 | La Convención | Santa Teresa   |     57 | M      |                 36 | Pasaje Inca 677      |
|          488 | Miguel Pérez Ccopa      | 42471302 | Urubamba      | Machu Picchu   |     50 | M      |                 42 | Urbanización Sol 52  |
|          489 | Pedro Apaza Chávez      | 37645352 | La Convención | Quillabamba    |     41 | M      |                 17 | Calle Principal 463  |
|          490 | Carmen Yupanqui Flores  | 68305637 | Paucartambo   | Kosñipata      |     72 | M      |                 35 | Urbanización Sol 140 |
|          491 | Carmen Apaza Condori    | 45096359 | La Convención | Echarate       |     81 | F      |                 26 | Calle Principal 117  |
|          492 | Luis Mamani Quispe      | 16604282 | Quispicanchi  | Oropesa        |     70 | M      |                 37 | Av. Libertad 783     |
|          493 | Ana Yupanqui Flores     | 22636044 | Urubamba      | Machu Picchu   |     46 | F      |                 24 | Urbanización Sol 76  |
|          494 | María Huamán Condori    | 94286111 | La Convención | Echarate       |     66 | M      |                 42 | Pasaje Inca 316      |
|          495 | María Ccopa Huamán      | 82379048 | La Convención | Quillabamba    |     84 | F      |                 41 | Jr. Los Héroes 797   |
|          496 | José Apaza Huamán       | 86729053 | Quispicanchi  | Urcos          |     84 | F      |                 20 | Pasaje Inca 841      |
|          497 | Luis Chávez Ccopa       | 55160555 | Calca         | Calca          |     62 | M      |                 40 | Av. Libertad 541     |
|          498 | Carmen Pérez Pérez      | 56336659 | Quispicanchi  | Oropesa        |     42 | F      |                 49 | Pasaje Inca 606      |
|          499 | Miguel Pérez Pérez      | 21702220 | Urubamba      | Ollantaytambo  |     79 | M      |                 32 | Urbanización Sol 366 |
|          500 | Rosa Pérez Quispe       | 71390177 | Quispicanchi  | Oropesa        |     27 | M      |                 41 | Pasaje Inca 229      |
