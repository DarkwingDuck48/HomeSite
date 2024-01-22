from typing import Any
from django import forms
from .models import Operation, Category
from budget.queries import get_all_category


class OperationForm(forms.ModelForm):
    operation_date = forms.DateField()
    category = forms.ModelChoiceField(queryset=get_all_category())
    amount = forms.DecimalField()
    operation_type = forms.ChoiceField(label="Тип категории", choices=Operation.OPER_TYPE_CHOICES)
    comment = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Operation
        fields = ("operation_date", "category", "operation_type", "amount", "comment")

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
        self.fields["operation_type"].widget.attrs["class"] = "form-select form-select-sm"
        self.fields["comment"].widget.attrs["class"] = "form-control"

class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        label="Имя категории",
        max_length=20,
        required=True
    )
    limit = forms.DecimalField(decimal_places=2, max_digits=8, required=False)

    class Meta:
        model = Category
        fields = ("name", "limit")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["class"] = "form-control form-control-sm"
        self.fields["name"].widget.attrs["placeholder"] = "Имя категории"
        self.fields["limit"].widget.attrs["class"] = "form-control form-control-sm"
        self.fields["limit"].widget.attrs["placeholder"] = "Лимит за период"
        
