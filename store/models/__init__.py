# store/models/__init__.py
from .category import Category
from .evento import Event  # <-- Importa Event (que es el nombre real en tu archivo)
from .profile import UserProfile
from .registration import Registration, RegistrationItem

__all__ = ['Category', 'Event', 'UserProfile', 'Registration', 'RegistrationItem']