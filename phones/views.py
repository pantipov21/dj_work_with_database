from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
	sort_method = request.GET.get('sort','id')
	template = 'catalog.html'
	context = {}
	if sort_method == 'name':
		context['phones'] = Phone.objects.all().order_by('name')
	elif sort_method == 'min_price':
		context['phones'] = Phone.objects.all().order_by('price')
	elif sort_method == 'max_price':
		context['phones'] = Phone.objects.all().order_by('-price')
	else:
		context['phones'] = Phone.objects.all()
	return render(request, template, context)


def show_product(request, slug):
	template = 'product.html'
	context = {}
	phones = Phone.objects.all()
	for p in phones:
		if p.slug == slug:
			context['phone'] = p
			break
	return render(request, template, context)
