"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include
# Estas son las importaciones necesarias para los tokens
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Aquí ya tienes tu conexión a store.urls
    path('api/', include('store.urls')),
    
    # Añadimos estas dos rutas para poder pedir el token de acceso en Postman
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]