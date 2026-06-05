from django.urls import path
from .views import EventoListAPIView, EventoDetailAPIView

urlpatterns = [
    path('eventos/', EventoListAPIView.as_view(), name='evento-list'),
    path('eventos/<int:pk>/', EventoDetailAPIView.as_view(), name='evento-detail'),
]