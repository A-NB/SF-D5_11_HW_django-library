from tabnanny import verbose
from django.apps import AppConfig


class PLibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'p_library'
    verbose_name = "Моя библиотека"
