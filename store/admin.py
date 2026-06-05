# store/admin.py
from django.contrib import admin
from .models import UserProfile, Event, Category  # 1. Importa Category aquí

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(Category) # 2. Registra el modelo Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name'] # Ajusta 'name' según cómo se llame el campo en tu modelo

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'price', 'capacity', 'is_active']
    list_filter = ['is_active', 'category']
    search_fields = ['title', 'description']