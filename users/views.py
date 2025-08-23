from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from .forms import CustomUserCreationForm

User = get_user_model()

# View de registro de usuário
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Listagem de usuários
@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

# Edição de usuário
class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'email', 'bio', 'birth_date']
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('user-list')

# Exclusão de usuário
class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('user-list')