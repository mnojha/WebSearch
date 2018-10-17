from django import forms

class SearchForm(forms.Form):
	product_name = forms.CharField(label='product_name',max_length=50)