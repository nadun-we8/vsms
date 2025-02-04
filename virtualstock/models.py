import uuid
from django.db import models
from item.models import SupplierStockItem

# Create your models here.

class VirtualStock(models.Model):
    virtual_stock_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    supplier_stock_item_id = models.OneToOneField(SupplierStockItem, on_delete=models.CASCADE)
    markup_amount = models.DecimalField(max_digits=10, decimal_places=2)
    listing_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'virtual_stock'
