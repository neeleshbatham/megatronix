from django.db import models
from datetime import date
import datetime
from django import forms
# Create your models here.

class Category(models.Model):
    """docstring for ClassName."""

    category_name = models.CharField( max_length=120,null=True,blank=True)
    image = models.ImageField(upload_to='category/images',default="",blank=False,null=False)    
    description = models.TextField(null=True,blank=True)
    slug = models.SlugField(unique=True,default="",null=False,blank=False)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.category_name)


class SubCategoryParent(models.Model):
    """docstring for ClassName."""

    category = models.ForeignKey(Category,null=True,blank=True)
    sub_cat_parent_name = models.CharField(max_length=120,null=True,blank=True)
    image = models.ImageField(upload_to='subcategoryparent/images',default="",blank=False,null=False)
    description = models.TextField(null=True,blank=True)
    slug = models.SlugField(unique=True,default="",null=False,blank=False)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        """Unicode class."""
        return str(self.sub_cat_parent_name)


class SubCategoryChild(models.Model):
    """docstring for ClassName."""

    sub_category_parent = models.ForeignKey(SubCategoryParent,null=True,blank=True)
    sub_cat_child_name = models.CharField(max_length=120,null=True,blank=True)
    image = models.ImageField(upload_to='products/images',default="",blank=False,null=False)
    description = models.TextField(null=True,blank=True)
    slug = models.SlugField(unique=True,default="",null=False,blank=False)
    active = models.BooleanField(default=True)
        

    def __unicode__(self):
        return str(self.sub_cat_child_name)


class Product(models.Model):
    """Product class."""

    # category = models.ForeignKey(Category,default="",null=False,blank=False)
    # sub_category_parent = models.ForeignKey(SubCategoryParent,default="",null=False,blank=False)
    sub_category_child = models.ForeignKey(SubCategoryChild,null=False,blank=False)
    title = models.CharField(max_length=120,null=False, blank=False) 
    image = models.ImageField(upload_to='products/images',default="",blank=False,null=False)
    description = models.TextField(null=True,blank=True)
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=True)
        

    def __unicode__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'slug')


class ProductImage(models.Model):
    """Product Image Class."""

    products = models.ForeignKey(Product,null=True,blank=True)
    image = models.ImageField(upload_to='products/images')
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)


    def __unicode__(self):
        return str(self.products)

class Enquiry(models.Model):

    content = models.TextField()
    name  = models.CharField( max_length=20)
    title = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=10, unique=True)
    created_date = models.DateField(auto_now_add=True)


    def __unicode__(self):
        return str(self.title)