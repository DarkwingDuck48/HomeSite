"""Logic for categories"""

from django.forms.utils import ErrorDict

from django.shortcuts import get_object_or_404
from budget.models import Category
from budget.forms import CategoryForm

__all__ = ["delete_category", "create_category"]


def create_category(form: CategoryForm) -> ErrorDict| None:
    if form.is_valid():
        category: Category = form.save(commit=False)
        category.save()
    else:
        return form.errors

def delete_category(category_id: int) ->None:
    category_to_delete = get_object_or_404(Category, pk=category_id)
    category_to_delete.delete()


def detail_category(category_id, year:int|None = None, month:int|None = None):
    category = get_object_or_404(Category, pk=category_id)
    
    
