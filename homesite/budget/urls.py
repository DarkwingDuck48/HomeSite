from django.urls import path
from . import views


app_name = "budget"
urlpatterns = [
    path("accounts", views.accounts, name="accounts"),
    path("details/<int:account_id>", views.detail_account, name="detail_account"),
]
