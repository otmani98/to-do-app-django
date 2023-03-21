from django import forms

class DoList(forms.Form):
    item = forms.CharField(max_length=100 , required=True)