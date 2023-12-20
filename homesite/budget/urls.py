from django.urls import path
from . import views


app_name = "budget"

urlpatterns = [
    path("", views.home, name="home"),
    path("details/<int:category_id>", views.detail_category, name="detail_category"),
    path("add_operation", views.add_operation, name='add_operation')
]
