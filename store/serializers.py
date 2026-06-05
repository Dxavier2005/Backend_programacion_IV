from rest_framework import serializers
from .models import Event, Category, Registration, RegistrationItem, UserProfile

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
        # Esto asegura que el usuario que registra sea asignado automáticamente
        read_only_fields = ['user']

class RegistrationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationItem
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'