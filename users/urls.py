from django.urls import path
from .views import register, user_list, UserUpdateView, UserDeleteView

urlpatterns = [
    path('register/', register, name='register'),
    path('list/', user_list, name='user-list'),
    path('edit/<int:pk>/', UserUpdateView.as_view(), name='user-edit'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
]