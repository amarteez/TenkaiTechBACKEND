# store/urls.py
from django.urls import path
from .views import ProductListView, CategoryListView, CartItemsView, AddToCartView, RemoveFromCartView, index, product_list, product_detail

urlpatterns = [
    path('products/categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:id>/', product_detail, name='product-detail'),
    path('cart/', CartItemsView.as_view(), name='cart-list'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/remove/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('', index, name='index'),
]
