# Tienda de camisetas de fútbol

Proyecto Django con CRUD de camisetas, carga de imágenes, carrito de compras y login.

## Cómo usar

1. Crear y activar el entorno virtual.
2. Instalar dependencias:
   ```bash
   python -m pip install -r requirements.txt
   python -m pip install Pillow
   ```
3. Ejecutar migraciones:
   ```bash
   python manage.py migrate
   ```
4. Correr el servidor:
   ```bash
   python manage.py runserver
   ```

## Pipeline

Se agregó GitHub Actions en `.github/workflows/django-ci.yml` que ejecuta:
- `python manage.py check`
- `python manage.py migrate --noinput`
- `python manage.py test`

## Notas

- Las imágenes se guardan en `media/`.
- Para cargar datos de prueba puedes usar el comando custom management `seed_shirts`.
