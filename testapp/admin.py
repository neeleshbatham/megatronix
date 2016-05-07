from django.contrib import admin
from .models import Category, SubCategoryParent, SubCategoryChild, Product, ProductImage,Enquiry



# class SubCategoryChildAdmin(ImportExportMixin, admin.ModelAdmin):
#     """SubCategoryChildAdmin."""
#     list_display = ['sub_category_parent', 'sub_cat_child_name']
#     prepopulated_fields = {"slug": ("sub_cat_child_name",)}

#     class Meta:
#         """Meta."""

#         model = SubCategoryChild


admin.site.register(Category)
admin.site.register(SubCategoryParent)
admin.site.register(SubCategoryChild)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Enquiry)
