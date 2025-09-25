from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserBase

@admin.register(UserBase)
class CustomUserAdmin(UserAdmin):
    # Campos exibidos na lista do admin
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "birth_date")
    
    # Campos disponíveis para pesquisa
    search_fields = ("username", "email", "first_name", "last_name")
    
    # Campos filtráveis na barra lateral
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    
    # Organização dos campos no formulário de edição
    fieldsets = UserAdmin.fieldsets + (
        ("Informações adicionais", {"fields": ("bio", "birth_date")}),
    )
    
    # Campos ao criar novo usuário
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Informações adicionais", {"fields": ("bio", "birth_date")}),
    )
