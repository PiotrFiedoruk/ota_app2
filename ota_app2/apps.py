from django.apps import AppConfig


class OtaApp2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ota_app2'

    def ready(self):
        import ota_app2.signals
