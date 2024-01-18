from django.apps import AppConfig


class BudgetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'budget'
    homesite_application = True
    homesite_tech_application = False
    application_home_url = "/budget"