from django.apps import AppConfig


class WinterarcConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'WinterArc'


    def ready(self):
        import WinterArc.signals
