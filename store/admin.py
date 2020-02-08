from django.contrib import admin
from .models import Category, SubCategory, Product
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.


class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'sub_category', 'date']
    list_filter = ['sub_category']
    search_fields = ['description', 'header']
    readonly_fields = ('date',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
