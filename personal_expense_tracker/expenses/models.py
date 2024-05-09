from django.db import models

class Expense(models.Model):
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    name  = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)





    def __str__(self):
        return f"{self.description} - {self.category} - ${self.amount}"
