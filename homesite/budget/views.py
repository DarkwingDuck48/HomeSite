from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.db.models import Sum, F, Value, CharField


import budget.logic as app_logic
import budget.queries as queries

from .models import Category, Operation, Period
from .forms import CategoryForm, OperationForm



def home(request):
    """Построение начального Dashboard по текущему состоянию бюджета."""
    period_today = queries.get_period()
    operations_credit, operations_debit = queries.get_operations_by_period_and_category_sum(period_today)
    sum_by_credit = operations_credit.aggregate(Sum("spend_by_category"))
    sum_by_debit = operations_debit.aggregate(Sum("get_by_category"))
    context = {
        "operations_credit": operations_credit,
        "operations_debit": operations_debit,
        "spend_all_category": sum_by_credit,
        "get_all_category": sum_by_debit,
        "rest_of_money": sum_by_debit["get_by_category__sum"] - sum_by_credit["spend_by_category__sum"],
        "today": datetime.now(),
        "period_today": period_today,
    }
    return render(request, "budget/dashboard.html", context)


def all_periods(request):
    context = {}
    return render(request, "budget/periods_settings.html", context)


def specify_period(request, period_id):
    return render(request, "budget/dashboard.html", context)

def all_categories(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Добавлена новая категория")
            return redirect("budget:categories")
        categories = Category.objects.all()
        context = {"categories": categories, "form": form}
        return render(request, "budget/categories.html", context)
    categories = Category.objects.all()
    form = CategoryForm()
    context = {"categories": categories, "form": form}
    return render(request, "budget/categories.html", context)


def delete_category(request, category_id):
    category_to_delete = get_object_or_404(Category, pk=category_id)
    category_to_delete.delete()
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
        form = OperationForm()

