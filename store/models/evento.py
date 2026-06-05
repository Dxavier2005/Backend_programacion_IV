import uuid
from pathlib import Path
from django.db import models
from .category import Category

def event_image_path(instance, filename):
    ext = Path(filename).suffix.lower()
    return f'events/{uuid.uuid4()}{ext}'

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    capacity = models.PositiveIntegerField(default=50)
    image = models.ImageField(upload_to=event_image_path, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='events')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    @property
    def has_cupos(self):
        return self.capacity > 0