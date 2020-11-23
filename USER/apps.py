from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'USER'

    def ready(self):
        import USER.signals
