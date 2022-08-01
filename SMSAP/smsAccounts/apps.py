from django.apps import AppConfig


class SmsaccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'smsAccounts'

    def ready(self):
        import smsAccounts.signals
