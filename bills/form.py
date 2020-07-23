from django.forms import ModelForm
from .models import Transaction

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['dt_transaction', 'description', 'value', 'category', 'observation']
