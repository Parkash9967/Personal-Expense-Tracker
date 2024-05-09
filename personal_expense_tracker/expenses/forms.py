from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["description", "category", "amount" , "name"]



class ExpenseCalculationForm(forms.Form):
    rent = forms.DecimalField(label="Rent Bill", max_digits=10, decimal_places=2)
    dukan = forms.DecimalField(label="Dukan Bill", max_digits=10, decimal_places=2)
    flat_expenses = forms.DecimalField(label="Flat Expenses", max_digits=10, decimal_places=2)
    net_bill = forms.DecimalField(label="Net Bill", max_digits=10, decimal_places=2)
    num_people = forms.IntegerField(label="Number of People", min_value=1)

