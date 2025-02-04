from rest_framework import serializers
from .models import StockItem, ItemCategory, SupplierStockItem
from supplier.models import Supplier

class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = ['item_category_id', 'item_category_name']

class StockItemSerializer(serializers.ModelSerializer):
    item_category = serializers.PrimaryKeyRelatedField(queryset=ItemCategory.objects.all())

    class Meta:
        model = StockItem
        fields = [
            'item_id', 'item_name', 'item_description', 'special_finishes',
            'yarn_count', 'moq', 'mcq', 'knitting_method', 'print', 'uom',
            'hsn_code', 'reorder_level', 'lead_time', 'item_color', 'item_category'
        ]

class SupplierStockItemSerializer(serializers.ModelSerializer):
    supplier_id = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    stock_item_id = serializers.PrimaryKeyRelatedField(queryset=StockItem.objects.all())


    class Meta:
        model = SupplierStockItem
        fields = ['supplier_id', 'stock_item_id', 'price', 'quantity']
