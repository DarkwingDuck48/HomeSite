from typing import Any
from django import forms
from .models import Operation, Category


class OperationForm(forms.ModelForm):
    operation_date = forms.DateField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    amount = forms.DecimalField()
    comment = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Operation
        fields = ("operation_date", "category", "amount", "comment")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["operation_date"].widget = forms.widgets.DateInput(
            attrs={
                "type": "date",
                "placeholder": "yyyy-mm-dd (DOB)",
                "class": "form-control",
            }
        )
        self.fields["category"].widget.attrs["class"] = "form-control"
        self.fields["amount"].widget.attrs["class"] = "form-control"
        self.fields["comment"].widget.attrs["class"] = "form-control"


class OperationCreditOnlyForm(OperationForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all().filter(cat_type="Cr"))
    
class OperationDebitOnlyForm(OperationForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all().filter(cat_type="Dr"))

class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        label="Имя категории",
        max_length=20,
        required=True
    )
    limit = forms.DecimalField(decimal_places=2, max_digits=8, required=False)
    cat_type = forms.ChoiceField(label="Тип категории", choices=Category.CAT_TYPE_CHOICES)

    class Meta:
        model = Category
        fields = ("name", "limit", "cat_type")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["class"] = "form-control form-control-sm"
        self.fields["name"].widget.attrs["placeholder"] = "Имя категории"
        self.fields["limit"].widget.attrs["class"] = "form-control form-control-sm"
        self.fields["limit"].widget.attrs["placeholder"] = "Лимит за период"
        self.fields["cat_type"].widget.attrs["class"] = "form-select form-select-sm"
