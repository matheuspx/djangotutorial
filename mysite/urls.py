from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('social.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('social/', include('social.urls')),
]
