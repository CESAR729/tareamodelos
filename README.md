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
El archivo **Suministros .CSV** contiene los siguientes campos clave:  
1. **Nombre de la Empresa**: Empresa de distribución eléctrica.  
2. **Región o Zona de Operación**: Área geográfica atendida.  
3. **SAIDI**: Índice de duración promedio de interrupciones (horas).  
4. **SAIFI**: Índice de frecuencia promedio de interrupciones (eventos).  
5. **Periodo de Medición**: Año, trimestre o mes.  
6. **Usuarios Totales Atendidos**: Cantidad de clientes atendidos.  
7. **Número Total de Interrupciones**: Cantidad de eventos de interrupción.  
8. **Duración Total de las Interrupciones**: Tiempo acumulado de interrupciones (en horas).  

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
