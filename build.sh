#!/usr/bin/env bash
# Exit on error
set -o errexit

# Variables de entorno para el superusuario
export DJANGO_SUPERUSER_USERNAME='admin'
export DJANGO_SUPERUSER_EMAIL='admin@example.com'
export DJANGO_SUPERUSER_PASSWORD='password123'

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Ejecutar el script de Python para crear el superusuario
python create_superuser.py