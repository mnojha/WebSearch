from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.template import loader
from .models import Product


# Create your views here.
def indexView(request):
	# Product.objects.all()
	list_ = Product.objects.all()
	description = Product.objects.all()
#	args = {'mylist' : list , 'description' : description}

	return render(request, 'mysearch/index.html', context={'mylist' : list_ , 'description' : description})
#	output = ', '.join([p.product_name for p in product_list, p.description for p in description])
#	template = loader.get_template('mysearch/index.html')
#	context = {
#		'product_list': product_list,
#		'description': description
#	}
#	return HttpResponse(template.render(context, request))
#	return HttpResponse(output)
#	return render(request, 'mysearch/index.html', context)

def detail(request, product_id):
	Product = get_object_or_404(Product, pk=product_id)
	return render(request, 'mysearch/detail.html', {'product': product})
#	return HttpResponse("looking at product %s." % product_id)

def search(request):
	#import pdb;pdb.set_trace()
	#product_name = request.GET['keyword']
	#product_name = input.get_attribute('value')
	product_name = request.GET.get('search', 'this is default')
	my_product = Product.objects.filter(product_name=product_name)
	#description = Product.objects.filter(product_name=product_name).values_list('description')
	#description = name.filter(description = name)
	#description = Product.objects.filter(description='name')
	#description = Product.objects.all()
	return render(request, 'mysearch/search.html', context={'my_product' : my_product})



	
