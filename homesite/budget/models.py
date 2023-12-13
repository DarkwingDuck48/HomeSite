from django.db import models

class Account(models.Model):
    """Account class"""
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'

class Category(models.Model):
    """Category Class"""
    name = models.CharField(max_length=20)
    limit = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self) -> str:
        return f'{self.name}'
    
class Operation(models.Model):
    """ Operation class"""
    operation_date = models.DateField(auto_now=True, auto_now_add=False)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    comment = models.CharField(max_length=250, null=True)
    