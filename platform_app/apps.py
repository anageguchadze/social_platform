from django.apps import AppConfig



class PlatformAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'platform_app'


    def ready(self):
        import platform_app.signals  