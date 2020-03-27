from django import forms
from django.core.validators import MinValueValidator

class FundTransferForm(forms.Form):
    fromAccountId = forms.IntegerField(validators=[MinValueValidator(1)])
    toAccountId = forms.IntegerField(validators=[MinValueValidator(1)])
    transferAmount = forms.FloatField(validators=[MinValueValidator(0.01)])

