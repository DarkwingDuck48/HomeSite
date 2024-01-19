from budget.forms import OperationForm
from budget.models import Operation, Period

__all__ = ["save_operation"]

def save_operation(form:OperationForm) -> None:
    operation: Operation = form.save(commit=False)
    operation.operation_period = Period.objects.filter(
        start_date__lte=operation.operation_date,
        end_date__gte=operation.operation_date,
    ).first()
    operation.save()
