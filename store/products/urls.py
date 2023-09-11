from django.urls import path
from products.views import *

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='products'),
    path('category/<int:category_pk>/', ProductsListView.as_view(), name='products'),
    path('baskets/<int:product_id>/', add_basket, name='add_basket'),
    path('remove_basket/<int:product_id>/', remove_basket, name='remove_basket')
]