# create_superuser.py

import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangocrud.settings')
django.setup()

User = get_user_model()

users = [
    {
        'username': os.getenv('DJANGO_SUPERUSER1_USERNAME'),
        'email': os.getenv('DJANGO_SUPERUSER1_EMAIL'),
        'password': os.getenv('DJANGO_SUPERUSER1_PASSWORD'),
    },
    {
        'username': os.getenv('DJANGO_SUPERUSER2_USERNAME'),
        'email': os.getenv('DJANGO_SUPERUSER2_EMAIL'),
        'password': os.getenv('DJANGO_SUPERUSER2_PASSWORD'),
    }
]

for user in users:
    if User.objects.filter(username=user['username']).exists():
        print(f"El usuario {user['username']} ya existe. No se creará un nuevo superusuario.")
    else:
        User.objects.create_superuser(username=user['username'], email=user['email'], password=user['password'])
        print(f"Superusuario {user['username']} creado exitosamente.")
