from django.db import models


class Category(models.Model):
    """Category Class"""

    name = models.CharField(max_length=20)
    limit = models.DecimalField(decimal_places=2, max_digits=8)

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

    operation_date = models.DateField(auto_now=False, auto_now_add=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    detalisation = models.JSONField(null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    comment = models.CharField(max_length=250, null=True)
    
    def __str__(self) -> str:
        return f"{self.operation_date}: {self.comment}"
