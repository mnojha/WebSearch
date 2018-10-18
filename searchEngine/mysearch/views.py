from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.template import loader
from .models import Product
from .models import Signup
from .forms import SearchForm
from .forms import SignupForm
from django.db.models import Q

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms


from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

# Create your views here.
def indexView(request):
	list_ = Product.objects.all()
#	description = Product.objects.all()
	form = SearchForm()
	return render(request, 'mysearch/index.html', context={'mylist' : list_ , 'form' : form})

def search(request):
	#import pdb;pdb.set_trace()
	#product_name = request.GET['keyword']
	product_name = request.GET.get('product_name', 'this is default')
	my_product = Product.objects.filter(product_name=product_name)
	return render(request, 'mysearch/search.html', context={'my_product' : my_product,})
	
#def signup(request):
#	if request.method == 'POST':
#		form = UserCreationForm(request.POST)
#		if form.is_valid:
#			form.save()
#			username = form.cleaned_data.get('username')
#			password = form.cleaned_data.get('password')
#			user = authenticate(username=username, password=password)
#			login(request,user)
#			return render('home')
#		else:
#			form = UserCreationForm()
#		return render(request, 'mysearch/signup.html', {'form': form})

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			username = userObj['username']
			password = userObj['password']
			if not(User.objects.filter(username=username).exists()):
				User.objects.create_user(username, password)
				user = authenticate(username=username, password=password)
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				raise forms.ValidationError('Looks like a username with that password already exists')

		else:
			form = UserCreationForm()
			return render(request, 'mysearch/signup.html', {'form': form})
# * the reason for using "reverse_lazy" instead of "reverse" is that for all generic
#  class_based views the urls are not loaded when the file is imported, so we have 
#  to use the lazy form of reverse to load them later when they're available. *


#	success_url = reverse_lazy('mysearch/index.html')
#	template_name = 'mysearch/signup.html'