from django import forms


class TreasureForm(forms.Form):
    name = forms.CharField(max_length=100)
    estimated_price = forms.IntegerField()
