from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.db import models
from django.conf import settings

from users.models import perfil
from .forms import CustomUserCreationForm
from django.conf import settings

User = get_user_model()

# View de criação de perfil
def create_perfil(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        data_nascimento = request.POST.get('data_nascimento')
        localizacao = request.POST.get('localizacao')
        interesses = request.POST.get('interesses')

        perfil_instance = perfil.objects.create(
            user=request.user,
            descricao=descricao,
            data_nascimento=data_nascimento,
            localizacao=localizacao,
            interesses=interesses
        )
        return redirect('user-list')
    return render(request, 'users/create_perfil.html')

class Perfil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    descricao = models.TextField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    localizacao = models.CharField(max_length=100, blank=True, null=True)
    interesses = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username