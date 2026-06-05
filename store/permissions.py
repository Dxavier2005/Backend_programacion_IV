# store/permissions.py
from rest_framework import permissions

class IsOrganizerOrReadOnly(permissions.BasePermission):
    """
    Permiso personalizado: Cualquiera puede ver (GET, HEAD, OPTIONS).
    Solo el organizador original puede editar (PUT) o borrar (DELETE).
    """
    def has_object_permission(self, request, view, obj):
        # Si la petición es de lectura (GET), se permite a cualquiera
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Si es de escritura (PUT, DELETE), el usuario debe ser el organizador asignado
        return obj.organizador == request.user