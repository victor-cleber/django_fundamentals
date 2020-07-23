from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=100)
    created_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "transactions"

    dt_transaction = models.DateTimeField()
    description = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    observation = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.description