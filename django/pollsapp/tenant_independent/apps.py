from django.apps import AppConfig


class TenantIndependentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tenant_independent'
