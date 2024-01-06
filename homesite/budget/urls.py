from django.urls import path
from . import views


app_name = "budget"

urlpatterns = [
    path("", views.home, name="home"),

    path("all_operation", views.all_operation, name='all_operation'),
    path("categories", views.all_categories, name="categories"),

    path("details/<int:category_id>", views.detail_category, name="detail_category"),

    path("delete_category/<int:category_id>", views.delete_category, name="delete_category"),
    path("delete_operation/<int:operation_id>", views.delete_operation, name="delete_operation"),
]
