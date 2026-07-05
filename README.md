# README — proyecto-final-automation-testing--Federico-Gomez-


## Propósito
Automatizar pruebas API requests con la API de [{JSON} Placeholder](https://jsonplaceholder.typicode.com/) .



## Tecnologías
- Python 3.10+  
- pytest  
- pytest-html (reportes)
- pip (gestor de dependencias)  
- Git (control de versiones)

## Requisitos previos
1. Python 3.10+ instalado.  

## Instalación de dependencias
1. Clonar el repositorio:
```bash
git clone git@github.com:SoldierGomez/proyecto-final-automation-testing--Federico-Gomez-.git
cd git@github.com:SoldierGomez/proyecto-final-automation-testing--Federico-Gomez-.git
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Cómo ejecutar las pruebas
1. Ejecutar todas las pruebas:
```bash
pytest 
```
## Cómo ejecutar el reporte

- El reporte se generara automaticamente al finalizarla ejecucion del comando previo:
```bash
pytest 
```


## Estructura del proyecto
- tests/                — casos de prueba 
- utils/                — helpers/utilidades (logger)
- conftest.py           — fixtures de pytest 
- reporte_Tests.html    — reporte
- requirements.txt      — dependencias


## Contribuir
1. Crear branch: feature/<descripcion>
2. Añadir tests y documentación.
3. Abrir PR y asignar revisores.
4. Asegurarse que CI pasa y los reportes se generan.

## Contacto
- Contacto: fedenogues@gmail.com