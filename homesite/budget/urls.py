from django.urls import path
from . import views


app_name = "budget"

urlpatterns = [
    path("", views.home, name="home"),

    path("operations", views.all_operation, name='operations'),
    path("operations/<int:year>/<int:month>", views.all_operation_by_period, name="operations_by_period"),
    path("operations/add/<str:category_type>", views.add_operation_from_dashboard, name="add_operation_dashboard"),
    path("categories", views.all_categories, name="categories"),
    
    path("periods", views.all_periods, name="periods"),
    path("details/<int:category_id>/<int:year>/<int:month>", views.detail_category_by_period, name="detail_category_by_period"),
    path("details/<int:category_id>", views.detail_category, name="detail_category"),

    path("delete_category/<int:category_id>", views.delete_category, name="delete_category"),
    path("delete_operation/<int:operation_id>", views.delete_operation, name="delete_operation"),
]
