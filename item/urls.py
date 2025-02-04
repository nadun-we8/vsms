from django.urls import path
from .views import item_category_list, item_category_detail, stock_item_list, stock_item_detail, supplier_stock_item_list, supplier_stock_item_detail

urlpatterns = [
    path('item-category/', item_category_list, name='item_category_list'),
    path('item-category/<uuid:pk>/', item_category_detail, name='item_category_detail'),
    path('stock-item/', stock_item_list, name='stock_item_list'),
    path('stock-item/<uuid:pk>/', stock_item_detail, name='stock_item_detail'),
    path('supplier-stock-item/', supplier_stock_item_list, name='supplier_stock_item_list'),
    path('supplier-stock-item/<int:pk>/', supplier_stock_item_detail, name='supplier_stock_item_detail'),
]
