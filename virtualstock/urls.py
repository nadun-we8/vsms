from django.urls import path
from .views import virtual_stock_list, virtual_stock_detail

urlpatterns = [
    path('virtual-stock/', virtual_stock_list, name='virtual_stock_list'),
    path('virtual-stock/<uuid:pk>/', virtual_stock_detail, name='virtual_stock_detail'),
]
