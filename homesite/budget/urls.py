from django.urls import path
from . import views


app_name = "budget"

urlpatterns = [
    path("", views.home, name="home"),
    path("categories", views.get_categories, name="categories"),
    path("details/<int:category_id>", views.detail_category, name="detail_category"),
    path("add_operation/<int:operation_id>", views.delete_operation, name="delete_operation"),
    path("add_operation", views.add_operation, name='add_operation')
]
