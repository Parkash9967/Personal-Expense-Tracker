from django.shortcuts import render, redirect, get_object_or_404, redirect
from .models import Expense
from .forms import ExpenseForm
from .forms import ExpenseCalculationForm
from django.db.models import Sum
from django.urls import reverse


def index(request):
    expenses = Expense.objects.all()
    return render(request, "expenses/index.html", {"expenses": expenses})

def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ExpenseForm()
    return render(request, "expenses/add_expense.html", {"form": form})

def expense_summary(request):
    # Get all expenses
    expenses = Expense.objects.all()

    # Calculate the total sum of all expenses
    total_expenses = expenses.aggregate(Sum("amount"))["amount__sum"] or 0.0

    # Calculate summary by category
    summary = {}
    for expense in expenses:
        category = expense.category
        if category not in summary:
            summary[category] = 0
        summary[category] += float(expense.amount)

    return render(
        request,
        "expenses/expense_summary.html",
        {"summary": summary, "total_expenses": total_expenses},
    )


def calculate_expenses(request):
    if request.method == "POST":
        form = ExpenseCalculationForm(request.POST)
        if form.is_valid():
            rent = form.cleaned_data["rent"]
            dukan = form.cleaned_data["dukan"]
            flat_expenses = form.cleaned_data["flat_expenses"]
            net_bill = form.cleaned_data["net_bill"]
            num_people = form.cleaned_data["num_people"]

            # Calculate total and divide by the number of people
            total = rent + dukan + flat_expenses + net_bill
            per_person = total / num_people

            return render(request, "expenses/calculate_expenses.html", {
                "form": form,
                "result": per_person,
                "total": total,
                "num_people": num_people
            })
    else:
        form = ExpenseCalculationForm()

    return render(request, "expenses/calculate_expenses.html", {"form": form})


def delete_expense(request, expense_id):
    # Get the expense or return a 404 if not found
    expense = get_object_or_404(Expense, id=expense_id)

    if request.method == "POST":
        expense.delete()
        # Redirect to the home page or another relevant page
        return redirect(reverse("index"))

    # Render a confirmation template if you want a safety check
    return render(request, "expenses/confirm_delete.html", {"expense": expense})



def search_expenses_by_buyer(request):
    name = request.GET.get("name", "")  # Get the buyer's name from query parameters
    expenses = Expense.objects.filter(name__icontains=name)  # Case-insensitive search
    total_amount = expenses.aggregate(Sum("amount"))["amount__sum"] or 0.0

    return render(
        request,
        "expenses/search_expenses_by_buyer.html",
        {"expenses": expenses, "total_amount": total_amount, "name": name},
    )