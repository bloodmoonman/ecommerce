from django.apps import AppConfig


class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecommerce.dashboard' #when I added "ecommerce.dashboard" as a new app in settings.py, I need to change this also, otherwise paths doesn't find dashboard files.
