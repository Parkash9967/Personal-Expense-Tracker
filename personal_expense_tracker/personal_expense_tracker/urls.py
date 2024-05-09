from django.contrib import admin
from django.urls import path
from expenses.views import index, add_expense, expense_summary, calculate_expenses, delete_expense, search_expenses_by_buyer

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("add_expense/", add_expense, name="add_expense"),
    path("expense_summary/", expense_summary, name="expense_summary"),
    path("calculate_expenses/", calculate_expenses, name="calculate_expenses"),
    path("delete_expense/<int:expense_id>/", delete_expense, name="delete_expense"),
    path("search_expenses_by_buyer/", search_expenses_by_buyer, name="search_expenses_by_buyer"),


]
