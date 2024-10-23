from django.contrib import admin
from django.urls import path
from expenseapp import views 

urlpatterns = [
    path('expenses/', views.CreateExpense.as_view(), name='expenses/'),
    path('totals/', views.ExpenseTotals.as_view(), name='totals/'),
    path('expenses/month/<int:year>/<int:month>/', views.MonthExpenses.as_view(), name='expenses/month/'),
]