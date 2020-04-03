from django import forms
from django.core.validators import MinValueValidator

class FundTransferForm(forms.Form):
    fromAccount = forms.IntegerField(validators=[MinValueValidator(1)])
    toAccount = forms.IntegerField(validators=[MinValueValidator(1)])
    transferAmount = forms.FloatField(validators=[MinValueValidator(0.01)])
    otp = forms.IntegerField(widget=forms.TextInput(attrs={'id': 'otpInput', 'type': 'tel', 'autofocus': 'true'}))

class FundDepositWithdrawForm(forms.Form):
    accountId = forms.IntegerField(validators=[MinValueValidator(1)])
    amount = forms.FloatField(validators=[MinValueValidator(0.01)])
    otp = forms.IntegerField(widget=forms.TextInput(attrs={'id': 'otpInput', 'type': 'tel', 'autofocus': 'true'}))
    