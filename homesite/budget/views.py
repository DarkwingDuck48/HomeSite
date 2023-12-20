from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Category, Operation
from .forms import OperationForm

# Create your views here.

def home(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "budget/categories.html", context)


def detail_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    operations = Operation.objects.all().filter(category=category_id)
    return render(
        request, "budget/category_detail.html", {"category": category, "operations": operations}
    )
    
def add_operation(request):
    operations = Operation.objects.all()
    if request.method == "POST":
        form = OperationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Added new Operation")
            return render(request, "budget/new_operation.html", {'form': form, 'operations': operations})
    else:
        form = OperationForm()
        return render(request, "budget/new_operation.html", {'form': form, 'operations': operations})
    return render(request, "budget/new_operation.html", {'form': form, 'operations': operations})

