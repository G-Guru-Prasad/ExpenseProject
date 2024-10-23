from django.db import models

# Create your models here.
class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    amount = models.FloatField()
    category = models.CharField(max_length=64)
    expense_timestamp =  models.DateTimeField()