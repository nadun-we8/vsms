from rest_framework import serializers
from .models import VirtualStock
from item.models import SupplierStockItem

class VirtualStockSerializer(serializers.ModelSerializer):
    supplier_stock_item_id = serializers.PrimaryKeyRelatedField(queryset=SupplierStockItem.objects.all())

    class Meta:
        model = VirtualStock
        fields = ['virtual_stock_id', 'supplier_stock_item_id', 'markup_amount', 'listing_price']
