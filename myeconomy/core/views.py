from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import DailyTransactionForm
from .models import DailyTransaction, Category



def dashboard(request):
    if request.method == 'POST':
        form = DailyTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse('form not good')
    else:
        form = DailyTransactionForm()
    

    transactions = DailyTransaction.objects.all()
    total_income = sum([transaction.amount  for transaction in DailyTransaction.objects.filter(inc_exp='Income')])
    total_expense = sum([transaction.amount  for transaction in DailyTransaction.objects.filter(inc_exp='Expense')])
    balance = total_income - total_expense

    paginator = Paginator(transactions, 3)
    page = request.GET.get('page')
    try:
        transactions = paginator.page(page)
    except PageNotAnInteger:
        transactions = paginator.page(1)
    except EmptyPage:
        transactions = paginator.page(paginator.num_pages)

    return render(request, 'dashboard.html', {'form': form,
                                              'transactions': transactions,
                                              'total_income':total_income,
                                              'total_expense':total_expense,
                                              'balance': balance,
                                              'page':page})


def filter_transaction(request):
    if request.is_ajax():
        from_date = datetime.strptime(request.GET.get('from_date', None), '%Y-%m-%d')
        to_date = datetime.strptime(request.GET.get('to_date', None), '%Y-%m-%d')
        results = DailyTransaction.objects.filter(date__range=[from_date, to_date])
        data = serializers.serialize('json', results)
        print(data)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype) 


def filter(request):
    return render(request, 'filter.html')


def visualize(request):
    categories = Category.objects.all()
    d = {}
    for category in categories:
        d.update({category.name: sum([transaction.amount  for transaction in DailyTransaction.objects.filter(category=category)])})
    print(d)
    return render(request, 'visualize.html', {'d':d})