import json
from django.conf.urls import url
from django.core.serializers.json import DjangoJSONEncoder
from tastypie import fields
from django.http.response import HttpResponse
from tastypie.http import HttpBadRequest
from tastypie.utils.urls import trailing_slash
from tastypie.resources import ModelResource

from .models import Product


class ProductResource(ModelResource):

    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'
        allowed_methods = ['get', 'post', 'put']
        always_return_data = True

    
    def prepend_urls(self):
        return [
                url(r"^(?P<resource_name>%s)/view-products%s" %(self._meta.resource_name, trailing_slash()), self.wrap_view('view_products'), name="view_products" )

				]
    def view_products(self, request, **kwargs):
        try:
            products = Product.objects.all()
            product_details = []
            for product in products:
                products = {}
                products['title'] = product.title
                products['product_category_id'] = product.description
                products['product_active'] = product.active
                product_details.append(products)
                print("procudtttttttttttttttdetail",product_details)
            return HttpResponse(json.dumps({'status_code':200, 'products': product_details}), content_type='application/json')
        except Exception as ex:
	    	print("except",ex)
	        return HttpBadRequest()