from django.apps import AppConfig


class AutoIncludeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auto_import'
