# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from . import models
from .api.BalanceFromAddress import BalanceFromAddress


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )


class ExchangeAccountForm(forms.ModelForm):
    class Meta:
        model = models.ExchangeAccount
        fields = ('key', 'secret', 'passphrase', )


class UserChangeDetailsForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30,
        required=False,
        help_text='<ul><li>Optional</li></ul>')
    last_name = forms.CharField(
        max_length=30,
        required=False,
        help_text='<ul><li>Optional</li></ul>')

    class Meta:
        model = models.User
        fields = ('first_name', 'last_name', )


class UserChangeFiatForm(forms.ModelForm):
    fiat = forms.ModelChoiceField(
        queryset=models.Fiat.objects.all(),
        empty_label=None,
        help_text='<ul><li>Preffered currency</li></ul>')

    class Meta:
        model = models.UserProfile
        fields = ('fiat', )


class ManualInputForm(forms.ModelForm):
    currency = forms.ModelChoiceField(
        queryset=models.Currency.objects.all(),
        empty_label=None)

    class Meta:
        model = models.ManualInput
        fields = ('currency', 'amount', )


class AddressInputForm(forms.ModelForm):
    currency = forms.ChoiceField(
        choices=BalanceFromAddress.getSupportedCurrencies())

    class Meta:
        model = models.AddressInput
        fields = ('currency', 'address', )

class InvestmentForm(forms.ModelForm):
    fiat = forms.ModelChoiceField(
            queryset=models.Fiat.objects.all(),
            empty_label=None,
            help_text='<ul><li>Invested fiat currency</li></ul>')

    class Meta:
        model = models.Investment
        fields = ('amount', 'fiat', )


class DeleteAccountForm(forms.ModelForm):
    confirm = forms.BooleanField(
            required=True,
            help_text="Check this box if you are sure you want to delete your account.")

    class Meta:
        model = models.User
        fields = ('confirm', )
