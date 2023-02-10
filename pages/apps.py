from django.apps import AppConfig


class PagesConfig(AppConfig): # will go into settings file
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
