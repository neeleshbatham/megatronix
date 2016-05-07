from django.shortcuts import render
from .models import Product, SubCategoryParent, SubCategoryChild, Category
from .forms import EnquiryForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import redirect
from django.shortcuts import render_to_response

def home(request):
	category = Category.objects.all()
	form = EnquiryForm()
	context = {'category':category, 
				'form':form}
	template = 'products/home.html'
	return render(request, template, context)


def sub_category(request, slug):
	category=Category.objects.get(slug=slug)
	subcategory= SubCategoryParent.objects.filter(category=category)
	context={'subcatparent':subcategory}
	template = 'products/subcategory.html'
	return render(request, template, context)



def sub_category_child(request, slug):
	# import ipdb; ipdb.set_trace()
	subcategoryparent=SubCategoryParent.objects.get(slug=slug)
	subcategorychild=SubCategoryChild.objects.filter(sub_category_parent=subcategoryparent)
	context={'subcatparentchild':subcategorychild}
	template='products/subcategorychild.html'
	return render(request, template, context)


def products(request, slug):
	# import ipdb; ipdb.set_trace()
	subcategorychild=SubCategoryChild.objects.get(slug=slug)
	products=Product.objects.filter(sub_category_child=subcategorychild)
	context={'products':products}
	template='products/product.html'
	return render(request, template, context)


def create(request):
	# import ipdb; ipdb.set_trace()
	form = EnquiryForm(request.POST or None)
	if (request.method=='POST'):
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			pass
	args = {}
	args.update(csrf(request))
	args['form']=form
	context={'args':args}
	template='form/create.html'
	return render(request, template, context)