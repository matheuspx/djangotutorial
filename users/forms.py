# users/forms.py
from django.contrib.auth.forms import UserCreationForm
from .models import UserBase

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserBase
        fields = ('username', 'email', 'bio', 'birth_date')