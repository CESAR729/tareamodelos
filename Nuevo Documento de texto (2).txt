# Código para generar README.md
readme_content = """
# Recaudación de Ingresos de Impuesto Predial 2023 de la Municipalidad Distrital de Parcona - [MDP]

## Economía y Finanzas

### Descripción
Información de ingresos de Tributos Municipales por concepto de Impuesto Predial, recaudados por la Municipalidad Distrital de Parcona, correspondiente al año 2023.

### Características
La Recaudación de Ingresos de Impuesto Predial está caracterizada por los siguientes datos:

- **Datos de la entidad:**
  - Departamento
  - Provincia
  - Distrito
  - Gobierno local de la entidad
  - Ubigeo

- **Datos del Contribuyente:**
  - Código del contribuyente anonimizado

- **Datos de los Tributos Municipales:**
  - Fecha de corte
  - Descripción del tributo
  - Año ordinario del tributo
  - Importe insoluto de pago
  - Importe del reajuste tributario
  - Importe de interés tributario
  - Derecho de emisión
  - Importe total de pago
  - Número de recibo
  - Fecha de pago

---

### Autor
**César Condori Huaychay**  
Universidad Nacional de San Antonio Abad del Cusco (UNSAAC)  
Carrera: Ingeniería Informática y de Sistemas
"""

# Guardar el contenido en el archivo README.md
try:
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print("README.md creado exitosamente.")
except Exception as e:
    print(f"Error al crear README.md: {e}")
