from django import forms
from .models import DailyTransaction


class DailyTransactionForm(forms.ModelForm):
    class Meta:
        model = DailyTransaction
        fields = '__all__'