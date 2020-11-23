from django.apps import AppConfig


class HomeConfig(AppConfig):
    name = 'HOME'

    def ready(self):
        import HOME.signals
