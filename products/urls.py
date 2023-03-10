from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
]