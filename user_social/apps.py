from django.apps import AppConfig


class UserSocialConfig(AppConfig):
    name = "user_social"

    def ready(self):
        import user_social.signals

