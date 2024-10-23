from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Expense
import json
from datetime import datetime as dt

# Create your views here.
class CreateExpense(APIView):
    def post(self, request):
        expense_name = request.data.get('name', '')
        expense_value = request.data.get('value', '')
        expense_category = request.data.get('category', '')

        try:
            expense_obj = Expense.objects.create(
                name = expense_name,
                amount = expense_value,
                category = expense_category,
                expense_timestamp = dt.now()
            )
            expense_obj.save()
            print('Expense record created successfully')
            return Response(data={'expense_id':expense_obj.expense_id}, status=200)
        except Exception as e:
            print('Unable to create expense record.Error - {0}'.format(str(e)))
            return Response(data={'msg':'Unable to create record'}, status=400)

    def get(self, request):
        try:
            expense_objs = Expense.objects.all()
            print('Expense records fetched')
        except Exception as e:
            print('Unable to create fetch records.Error - {0}'.format(str(e)))
            return Response(data={'msg':'Unable to fetch records'}, status=400)
        
        expense_data = []
        for each_expense in expense_objs:
            expense_data.append({
                'expense_id':each_expense.expense_id,
                'name':each_expense.name,
                'amount':each_expense.amount,
                'category':each_expense.category,
            })
        return Response(data=expense_data, status=201)


class MonthExpenses(APIView):
    def get(self, request,year, month):
        print('year', year, month)
        try:
            expense_obj = Expense.objects.filter(expense_timestamp__year=year)
            expense_obj = expense_obj.filter(expense_timestamp__month=month)
        except Exception as e:
            print('Unable to create fetch records.Error - {0}'.format(str(e)))
            return Response(data={'msg':'Unable to fetch records'}, status=400)
        
        expense_data = []
        for each_expense in expense_obj:
            expense_data.append({
                'expense_id':each_expense.expense_id,
                'name':each_expense.name,
                'amount':each_expense.amount,
                'category':each_expense.category,
            })
        return Response(data=expense_data, status=201)

class ExpenseTotals(APIView):
    def get(self, request):
        try:
            expense_objs = Expense.objects.all()
            print('Expense records fetched')
        except Exception as e:
            print('Unable to create fetch records.Error - {0}'.format(str(e)))
            return Response(data={'msg':'Unable to fetch records'}, status=400)
        expense_total = sum(expense_objs.values_list('amount', flat=True))

        return Response(data={'expense_total':expense_total}, status=201)
