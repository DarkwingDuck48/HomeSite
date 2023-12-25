from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.db.models import Sum
from .models import Category, Operation
from .forms import OperationForm

# Create your views here.


def home(request):
    context = {}
    return render(request, "budget/dashboard.html", context)

def get_categories(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "budget/categories.html", context)


def detail_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    operations = Operation.objects.all().filter(category=category_id)
    return render(
        request,
        "budget/category_detail.html",
        {"category": category, "operations": operations},
    )

def delete_operation(request, operation_id):
    operation_to_delete = get_object_or_404(Operation, pk=operation_id)
    operation_to_delete.delete()
    return redirect('budget:add_operation')


def add_operation(request):
    operations = Operation.objects.all()
    sum_all_operations = Operation.objects.aggregate(all_sum = Sum("amount"))
    if request.method == "POST":
        form = OperationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Added new Operation")
            sum_all_operations = Operation.objects.aggregate(
                all_sum = Sum("amount")
                )
            return redirect('budget:add_operation')
    else:
        form = OperationForm()
        return render(
            request,
            "budget/new_operation.html",
            {"form": form, "operations": operations, "all_sum": sum_all_operations["all_sum"]},
        )
    return render(
        request, "budget/new_operation.html", {"form": form, "operations": operations , "all_sum": sum_all_operations["all_sum"]}
    )
