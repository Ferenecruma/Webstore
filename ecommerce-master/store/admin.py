from django.contrib import admin
from .models import Category, SubCategory, Product
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class CategoryAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ['name', 'slug']


class SubCategoryAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ['name', 'slug']


class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ['name', 'sub_category', 'date']
    list_filter = ['sub_category']
    search_fields = ['description', 'header']
    readonly_fields = ('date',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
