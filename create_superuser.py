# create_superuser.py

import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tu_proyecto.settings')
django.setup()

User = get_user_model()

username = os.getenv('DJANGO_SUPERUSER_USERNAME')
email = os.getenv('DJANGO_SUPERUSER_EMAIL')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

if User.objects.filter(username=username).exists():
    print('El usuario ya existe. No se creará un nuevo superusuario.')
else:
    User.objects.create_superuser(username=username, email=email, password=password)
    print('Superusuario creado exitosamente.')
