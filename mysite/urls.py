from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from social import views as social_views # Importa as views do app social   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('social/', include('social.urls')),
    path('', social_views.home, name='root_home'),  # ✅ expõe o home direto
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
