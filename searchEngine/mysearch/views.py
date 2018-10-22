from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.template import loader
from .models import Product
from .forms import SearchForm
from .forms import SignupForm
from .forms import LoginForm
from django.db.models import Q

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms


from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
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
	
def signup(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		print(username)
		email = request.POST.get('email')
		print(email)
		password1 = request.POST.get('password1')
		print(password1)
		password2 = request.POST.get('password2')
		if password1 == password2:
			user = User.objects.create_user(username=username, email=email, password=password1,)
			user.save()
			print(signup)
			return HttpResponseRedirect("/")
		else:
			error = " Password Mismatch "
			return render(request, 'mysearch/signup.html',{"error":error})
	else:
		return render(request, 'mysearch/signup.html')
	

# * the reason for using "reverse_lazy" instead of "reverse" is that for all generic
#  class_based views the urls are not loaded when the file is imported, so we have 
#  to use the lazy form of reverse to load them later when they're available. *


#	success_url = reverse_lazy('mysearch/index.html')
#	template_name = 'mysearch/signup.html'

def user_login(request):
	form = LoginForm()
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			login(request,user)
			return HttpResponseRedirect("/signup")
		else:
			error = "Sorry! username and password didn't match, Please try again!"
			return render(request, 'mysearch/login.html')

	else:
		return render(request, 'mysearch/login.html')

