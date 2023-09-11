from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView

from products.models import *
# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = 'products/index.html'


class ProductsListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        if self.kwargs.get('category_pk'):
            return Product.objects.filter(category_id=self.kwargs.get('category_pk'))
        return super().get_queryset()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
@login_required(login_url=reverse_lazy('users:login'))
def add_basket(request, product_id):
    product = Product.objects.get(pk=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets:
        Basket.objects.create(product=product, user=request.user, quantity=1)
    else:
        basket = baskets[0]
        basket.quantity += 1
        basket.save()
    return redirect(request.META['HTTP_REFERER'])

def remove_basket(request, product_id):
    baskets = Basket.objects.filter(product_id=product_id)
    baskets.delete()
    return redirect(request.META['HTTP_REFERER'])