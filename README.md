# integration-test-free-market

## Setup

### Instalación

Previamente debe tener instalador python 3.10 o superior por compatibilidad. Si se encuentra en Windows debe configurar correctamente el Path, para mayor información visitar el sitio web [Python](https://www.python.org/). 

Luego se debe instalar las siguientes dependencias

- pip install pytest
- pip install requests

### Microservicios

Se debe tener levantado los servicios product-sale-free-market y seller-user-free-market para el correcto funcionamiento.

### Ejecución

Para ejecutar los tests bastará con ejecutar el comando `pytest /tests` en una terminal bash, si se encuentra en Windows el comando es `pytest .\tests\`

## Estructura

Cuenta con una carpeta `tests` en el cual internamente hay tres archivos:
- tests_rest_integration.py: Archivo principal que contará con los tests de integración esenciales
    - test_creacion_producto_ok
    - test_creacion_vendedor_error_mismo_request
    - test_creacion_venta_ok
- request_generator.py: Archivo con funciones para abstraer la creación de los requests
- utils_generator.py: Archivo con funciones utilitarias generales.