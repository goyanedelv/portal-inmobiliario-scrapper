# Scrappeador de portalinmobiliario.cl

__Work in progress__

### Carpetas relevantes
- `data/seed`: semillas para empezar a scrapear (manual).
- `data/raw_output`: información de las propiedades en `txt`.

### Parámetros
- `parametros.yaml`: archivo de configuración para establecer ubicación de `chromedriver` y nivel de tolerancia (cuántos errores aceptamos antes de abortar el scrapping de un archivo semilla).

### Dependencias relevantes
- `selenium`

### Cómo correrlo?

Scrappear a partir de la semilla:
```shell
> python code/portal_inmobiliario.py super_seed.txt
```

Generar base de datos:
```shell
> python code/raw_to_excel.py
```