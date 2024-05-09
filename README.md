# Personal-Expense-Tracker


This is a Django-based web application that allows users to track personal expenses, categorize them, calculate expenses, and view summaries. The application also provides features to calculate total expenses by buyer's name and delete expenses from the list.

## Features
- Add new expenses with descriptions, categories, buyer's name, and amount.
- View a list of all expenses.
- Calculate the expense per person based on specific bills.
- Calculate and view expense summaries with category-wise breakdowns.
- Search expenses by buyer's name and calculate the total amount bought by each buyer.
- Delete expenses from the list.

## Project Structure
```plaintext
personal_expense_tracker/
├── personal_expense_tracker/  # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── expenses/  # Django app with core functionality
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/  # HTML templates
│   │   ├── expenses/
│   │   │   ├── base.html
│   │   │   ├── index.html
│   │   │   ├── add_expense.html
│   │   │   ├── expense_summary.html
│   │   │   └── search_expenses_by_buyer.html
│   ├── tests.py
│   ├── views.py
│   ├── forms.py
│   └── static/  # Static files for CSS and JavaScript
│       └── style.css
├── db.sqlite3  # SQLite database
└── manage.py




Usage
* To add a new expense, click "Add Expense" on the home page, fill in the form, and submit.
* To view all expenses, visit the home page.
* To calculate the total expenses by buyer's name, use the search form on the home page.
* To view an expense summary, visit "Expense Summary" from the navigation menu.
* To delete an expense, click the "Delete" button next to the corresponding expense in the list.



