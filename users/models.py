from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    foto = models.ImageField(null=True, default='images/perfil.jpeg', upload_to='users')
    fondo = models.ImageField(null=True, default='images/default.jpg', upload_to='users_fondo')
    private = models.BooleanField(default=False)

    class Meta:
        db_table = 'USER'

    def __str__(self):
        return f'{self.email}--{self.id}'
