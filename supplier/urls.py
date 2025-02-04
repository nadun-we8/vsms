from django.urls import path
from .views import supplier_list, supplier_detail, supplier_category_list, supplier_category_detail

urlpatterns = [
    path('supplier/', supplier_list, name='supplier_list'),
    path('supplier/<int:pk>/', supplier_detail, name='supplier_detail'),
    path('supplier-category/', supplier_category_list, name='supplier_category_list'),
    path('supplier-category/<int:pk>/', supplier_category_detail, name='supplier_category_detail'),
]