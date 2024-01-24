from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.db.models import Sum


import budget.logic as app_logic
import budget.logic.queries as queries

from .models import Category, Operation, Period, BankAccount
from .forms import CategoryForm, OperationForm, BankAccountForm



def home(request):

    """Построение начального Dashboard по текущему состоянию бюджета."""
    context = app_logic.homepage_data()
    return render(request, "budget/dashboard.html", context)

# Periods

def all_periods(request):
    context = {}
    return render(request, "budget/periods_settings.html", context)

def specify_period(request, period_id):
    return render(request, "budget/dashboard.html", context)

# Category

def all_categories(request):
    if request.method == "POST":
        errors = app_logic.create_category(CategoryForm(request.POST))
        if errors:
            for err in errors:
                messages.error(request, f"{err}")
        else:
            messages.success(request, "Добавлена новая категория")
        return redirect("budget:categories")
    categories = queries.get_all_category()
    form = CategoryForm()
    context = {"categories": categories, "form": form}
    return render(request, "budget/categories.html", context)

def delete_category(request, category_id):
    app_logic.delete_category(category_id)
    return redirect("budget:categories")

def detail_category_by_period(request, category_id, year, month):
    category = get_object_or_404(Category, pk=category_id)
    period = queries.get_period_by_year_month(year, month)
    operations = queries.get_operations_by_period(period).filter(category=category_id).order_by("operation_date")
    return render(
        request,
        "budget/category_detail.html",
        {"category": category, "operations": operations, "period": period},
    )

def detail_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    operations = (
        Operation.objects.all().filter(category=category_id).order_by("operation_date")
    )
    return render(
        request,
        "budget/category_detail.html",
        {"category": category, "operations": operations, "period": "Все периоды"},
    )

# Operations

def edit_operation(request, operation_id):
    # ! TODO: MAKE REDIRECT WORK !!!
    edit_operation = get_object_or_404(Operation, pk=operation_id)
    form = OperationForm(request.POST or None, instance=edit_operation)
    if form.is_valid():
        app_logic.save_operation(form)
        return redirect("budget:operations")
    return render(request, "budget/edit_operation.html", 
                  context={"form":form, "edit_operation": edit_operation})
        

def delete_operation(request, operation_id):
    operation_to_delete = get_object_or_404(Operation, pk=operation_id)
    operation_to_delete.delete()
    return redirect(request.META.get("HTTP_REFERER"))

def all_operation_by_period(request, year, month):
    period = queries.get_period_by_year_month(year, month)
    operations = queries.get_operations_by_period(period).order_by("operation_date", "category")
    sum_all_operations = queries.get_operations_by_period(period).aggregate(all_sum=Sum("amount"))
    if request.method == "POST":
        form = OperationForm(request.POST)
        if form.is_valid():
            app_logic.save_operation(form)
            messages.success(request, "Added new Operation")
            sum_all_operations = Operation.objects.aggregate(all_sum=Sum("amount"))
            return redirect("budget:operations")
    else:
        form = OperationForm()
        return render(
            request,
            "budget/operations.html",
            {
                "form": form,
                "operations": operations,
                "all_sum": sum_all_operations["all_sum"],
            },
        )
    return render(
        request,
        "budget/operations.html",
        {
            "form": form,
            "operations": operations,
            "all_sum": sum_all_operations["all_sum"],
        },
    )

def all_operation(request):
    today = datetime.now()
    return all_operation_by_period(request, today.year, today.month)

def add_operation_from_dashboard(request):
    if request.method == "POST":
        form = OperationForm(request.POST)
        if form.is_valid():
            app_logic.save_operation(form)
            messages.success(request, "Added new Operation")
            return redirect("budget:home")
    else:
        form = OperationForm()
        return render(request, "budget/edit_operation.html", {"form": form})

# Bank

def all_bank_accounts(request):
    accounts = queries.get_all_bank_accounts()
    if request.method == "POST":
        form = BankAccountForm(request.POST)
        if form.is_valid():
            app_logic.save_bank_account(form, request.user)
            messages.success(request, "Added new Bank Account")
            return redirect("budget:bank_accounts")
    else:
        form = BankAccountForm()
        return render(request, "budget/bank_account.html", {"form": form, "accounts": accounts})

def delete_account(request, account_id):
    get_object_or_404(BankAccount, pk=account_id).delete()
    return redirect(request.META.get("HTTP_REFERER"))