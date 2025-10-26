# users/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Perfil

# receiver decorador vincula a função ao sinal post_save
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def criar_perfil_usuario(sender, instance, created, **kwargs):
    """
    Cria um perfil automaticamente sempre que um novo usuário é criado.
    """
    if created:
        Perfil.objects.create(user=instance)
