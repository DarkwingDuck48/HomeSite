from datetime import datetime

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.db.models import Sum, F, Value, CharField
from django.db.models.functions import Concat, ExtractYear, ExtractMonth

from .models import Category, Operation
from .forms import CategoryForm, OperationForm


def get_operation_periods() -> list[str]:
    periods = (
        Operation.objects
        .annotate(
            period_name=Concat(
                ExtractYear("operation_date"),
                Value("-"),
                ExtractMonth("operation_date"),
                output_field=CharField(),
            )
        )
        .values("period_name")
        .distinct()
    )
    return [period["period_name"] for period in periods]

def home(request):
    """Построение начального Dashboard по текущему состоянию бюджета."""
    periods = get_operation_periods()
    context = {"periods": periods}
    today = datetime.now()
    operations_sum = (
        Operation.objects.all()
        .filter(operation_date__year=today.year, operation_date__month=today.month)
        .values("category", "category__name", "category__limit")
        .annotate(rest_by_category=F("category__limit") - Sum("amount"), spend_by_category=Sum("amount"))
    )
    context.update({"operations_sum": operations_sum, "today":today})
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


def detail_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    operations = (
        Operation.objects.all().filter(category=category_id).order_by("operation_date")
    )
    return render(
        request,
        "budget/category_detail.html",
        {"category": category, "operations": operations},
    )


def delete_operation(request, operation_id):
    operation_to_delete = get_object_or_404(Operation, pk=operation_id)
    operation_to_delete.delete()
    return redirect("budget:all_operation")


def all_operation(request):
    operations = Operation.objects.all().order_by("operation_date", "category")
    sum_all_operations = Operation.objects.aggregate(all_sum=Sum("amount"))
    if request.method == "POST":
        form = OperationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Added new Operation")
            sum_all_operations = Operation.objects.aggregate(all_sum=Sum("amount"))
            return redirect("budget:all_operation")
    else:
        form = OperationForm()
        return render(
            request,
            "budget/all_operation.html",
            {
                "form": form,
                "operations": operations,
                "all_sum": sum_all_operations["all_sum"],
            },
        )
    return render(
        request,
        "budget/all_operation.html",
        {
            "form": form,
            "operations": operations,
            "all_sum": sum_all_operations["all_sum"],
        },
    )
