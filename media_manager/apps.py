from django.apps import AppConfig


class MediaManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'media_manager'
    verbose_name = 'Media'

    def ready(self):
        import media_manager.signals
