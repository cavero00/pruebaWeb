#!/usr/bin/env bash
# Exit on error
set -o errexit

# Variables de entorno para el primer superusuario
export DJANGO_SUPERUSER1_USERNAME='admin1'
export DJANGO_SUPERUSER1_EMAIL='admin1@example.com'
export DJANGO_SUPERUSER1_PASSWORD='password123'

# Variables de entorno para el segundo superusuario
export DJANGO_SUPERUSER2_USERNAME='admin2'
export DJANGO_SUPERUSER2_EMAIL='admin2@example.com'
export DJANGO_SUPERUSER2_PASSWORD='password456'

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Ejecutar el script de Python para crear el superusuario
python create_superuser.py