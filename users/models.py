# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserBase(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

from django.conf import settings

class Perfil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    localizacao = models.CharField(max_length=100, blank=True, null=True)
    interesses = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username