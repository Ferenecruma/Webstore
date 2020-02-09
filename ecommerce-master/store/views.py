from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from django.db.models import Count, Q
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

from store.models import Product, Category, SubCategory
from sendemail.forms import ContactForm

class HomeView(ListView):
    template_name = 'home.html'
    model = Category

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoriesView(ListView):
    template_name = 'categories.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SubCategoriesView(ListView, SingleObjectMixin):
    template_name = 'sub-categories.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(
            queryset=Category.objects.all())
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return SubCategory.objects.filter(category=self.object)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DetailsView(ListView):
    template_name='detail.html'
    
    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        form = ContactForm
        context = super().get_context_data(**kwargs)
        context['form'] = form
        return context