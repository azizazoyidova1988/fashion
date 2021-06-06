from django import forms
from .models import Billing_Address


class Billing_AddressForm(forms.ModelForm):
    class Meta:
        model = Billing_Address()
        fields = "__all__"