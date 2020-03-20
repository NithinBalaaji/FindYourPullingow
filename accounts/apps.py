from django.apps import AppConfig


class accountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals
