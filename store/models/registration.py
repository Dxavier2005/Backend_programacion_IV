# store/models/registration.py
from django.db import models
from django.contrib.auth.models import User
from .evento import Event  # <-- Corregido: Importa desde .evento

class Registration(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('confirmed', 'Confirmado'),
        ('cancelled', 'Cancelado'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Inscripción #{self.id} - {self.user.username}'

    def calculate_total(self):
        self.total = sum(item.subtotal for item in self.items.all())
        self.save(update_fields=['total'])


class RegistrationItem(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='items')
    # <-- Corregido: Agregamos la relación con Event para que funcione self.event.title
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registration_items', null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def subtotal(self):
        return self.unit_price * self.quantity

    def __str__(self):
        # Ahora que el campo 'event' existe, esto ya no dará error
        return f'{self.quantity}x {self.event.title if self.event else "Sin Evento"}'