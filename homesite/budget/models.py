from django.db import models



class Period(models.Model):
    """Periods Class"""
    name = models.CharField(max_length=20, unique=True)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    year = models.IntegerField()
    month = models.IntegerField()
    short_name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.name}"


class Category(models.Model):
    """Category Class"""

    name = models.CharField(max_length=20, unique=True)
    limit = models.DecimalField(decimal_places=2, max_digits=8, null=True)

    def __str__(self) -> str:
        return f"{self.name}"


class DetalisationDimension(models.Model):
    """ User dimensions class """
    name = models.CharField(max_length=30)


class DetalisationDimensionItem(models.Model):
    """ User dimensions items"""
    name = models.CharField(max_length=30)
    parent_id = models.IntegerField(default=-1)
    dim_id = models.ForeignKey(DetalisationDimension, on_delete=models.PROTECT)

class Operation(models.Model):
    """Operation class"""

    DEBIT = "Dr"
    CREDIT = "Cr"

    OPER_TYPE_CHOICES = {
        DEBIT: "Доход",
        CREDIT: "Расход"
    }

    operation_date = models.DateField(auto_now=False, auto_now_add=False)
    operation_period = models.ForeignKey(Period, on_delete=models.PROTECT, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    operation_type = models.CharField(max_length=2, choices=OPER_TYPE_CHOICES, default=CREDIT)
    detalisation = models.JSONField(null=True, blank=True)
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    comment = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.operation_date}: {self.comment}"
