from django import forms

class SearchForm(forms.Form):
	product_name = forms.CharField(label='product_name',max_length=50)

class SignupForm(forms.Form):
	username = forms.CharField(required = True,label='username', max_length=50)
	email = forms.EmailField(required = True,label='email')
	password = forms.CharField(required = True,label='password', max_length=50)

class LoginForm(forms.Form):
	username = forms.CharField(required = True,label='username', max_length=50)
	password = forms.CharField(required = True,label='password', max_length=50)


