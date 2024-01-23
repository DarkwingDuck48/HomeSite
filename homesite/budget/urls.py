from django.urls import path
from . import views


app_name = "budget"

urlpatterns = [
    path("", views.home, name="home"),

    path("operations", views.all_operation, name='operations'),
    path("operations/add", views.add_operation_from_dashboard, name="add_operation_dashboard"),
    path("operations/<int:operation_id>", views.edit_operation, name="edit_operation"),
    path("operations/<int:year>/<int:month>", views.all_operation_by_period, name="operations_by_period"),
    path("categories", views.all_categories, name="categories"),
    
    path("periods", views.all_periods, name="periods"),
    path("details/<int:category_id>/<int:year>/<int:month>", views.detail_category_by_period, name="detail_category_by_period"),
    path("details/<int:category_id>", views.detail_category, name="detail_category"),

    path("delete_category/<int:category_id>", views.delete_category, name="delete_category"),
    path("delete_operation/<int:operation_id>", views.delete_operation, name="delete_operation"),
    path("delete_account/<int:account_id>", views.delete_account, name="delete_account"),
    
    path("bank_accounts", views.all_bank_accounts, name="bank_accounts"),
]
