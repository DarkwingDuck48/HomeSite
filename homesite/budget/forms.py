from typing import Any
from django import forms
from .models import Operation, Category

class OperationForm(forms.ModelForm):

    operation_date = forms.DateField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    amount = forms.DecimalField()
    comment = forms.CharField(max_length=100)

    class Meta:
        model = Operation
        fields = ('operation_date', 'category', 'amount', 'comment')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['operation_date'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )
        self.fields['category'].widget.attrs['class'] = 'form-control'
        self.fields['amount'].widget.attrs['class'] = 'form-control'
        self.fields['comment'].widget.attrs['class'] = 'form-control'
        