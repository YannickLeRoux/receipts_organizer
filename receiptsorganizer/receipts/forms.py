from django import forms

from .models import Category, Receipt


class CategoryForm(forms.ModelForm):

    class Meta:
        fields = ('name',)
        model = Category


class NewReceiptForm(forms.Form):
    
    scan = forms.ImageField(label='Upload a Receipt Scan')

    class Meta():
        model= Receipt
        fields = ('category','name','amount','scan')
