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

	
