from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class DailyTransaction(models.Model):

    INC_EXP_CHOICES = (
        ("Income", "Income"),
        ("Expense", "Expense"),
    )

    date = models.DateTimeField()
    updated_date = models.DateTimeField()
    inc_exp = models.CharField('Income/Expense', max_length=10, choices=INC_EXP_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.category.name + str(self.amount)