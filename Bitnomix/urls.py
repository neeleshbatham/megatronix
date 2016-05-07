"""Bitnomix URL Configuration"""
"""Url Configurations"""

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from tastypie.api import Api

from testapp.api import ProductResource

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(ProductResource())

urlpatterns = patterns('',
    url(r'^$', 'testapp.views.home', name='home'),
    url(r'^subcategory/(?P<slug>[\w-]+)/$', 'testapp.views.sub_category', name='sub_category'),
    url(r'^subcategorychild/(?P<slug>[\w-]+)/$', 'testapp.views.sub_category_child', name='sub_category_child'),
    url(r'^products/(?P<slug>[\w-]+)/$', 'testapp.views.products', name='products'),
    
    url(r'^api/', include(v1_api.urls)),
    url(r'^create/',  'testapp.views.create', name='create'),

    url(r'^admin/', include(admin.site.urls)),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
