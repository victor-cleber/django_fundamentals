from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import Transaction
from .form import TransactionForm


def home(request):
    data = {}
    data['now'] = datetime.datetime.now()
    data['msg'] = "Hello World!"
    data['transactions'] = ['transaction 1', 'transaction 2', 'transaction 3']
    # html = "<html><body> It is now %s. </body></html>" %now
    # return HttpResponse(html)
    return render(request, 'bills/home.html', data)

def list_transactions(request):
    data = {}
    data['transactions'] = Transaction.objects.all() #filter, last, first

    return render(request, 'bills/transactions.html', data)

def new_transaction(request):
    form = TransactionForm(request.POST or None)
    #data['form'] = form

    if form.is_valid():
        form.save()
        return redirect('list')

    return render(request, 'bills/transaction.html', {'form': form})

def update_transaction(request, pk):
    data = {}
    transaction = Transaction.objects.get(pk=pk)
    form = TransactionForm(request.POST or None, instance=transaction)

    if form.is_valid():
        form.save()
        return redirect('list')

    data['form'] = form
    data['transaction'] = transaction
    return render(request, 'bills/transaction.html', data)

def delete_transaction(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    transaction.delete()
    return redirect('list')


