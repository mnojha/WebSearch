from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.template import loader
from .models import Product
from .forms import SearchForm
from django.db.models import Q

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


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
	
def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid:
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request,user)
			return redirect('home')
		else:
			form = UserCreationForm()
		return render(request, 'mysearch/signup.html', {'form': form})
