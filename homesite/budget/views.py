from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Operation


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
