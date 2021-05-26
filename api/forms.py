from django import forms

class CreateNewList(forms.Form):
    cidade = forms.CharField(label="Cidade", max_length=40)