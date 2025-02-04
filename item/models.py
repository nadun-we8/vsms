import uuid
from django.db import models
from supplier.models import Supplier

class ItemCategory(models.Model):
    item_category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item_category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.item_category_name

    class Meta:
        db_table = 'item_category'

class StockItem(models.Model):
    item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item_name = models.CharField(max_length=255)
    item_description = models.TextField()
    special_finishes = models.TextField()
    yarn_count = models.CharField(max_length=255)
    moq = models.IntegerField()  # Minimum Order Quantity
    mcq = models.IntegerField()  # Minimum Color Quantity
    knitting_method = models.CharField(max_length=255)
    print = models.CharField(max_length=255)
    uom = models.CharField(max_length=50)  # Unit of Measure
    hsn_code = models.CharField(max_length=255)
    reorder_level = models.IntegerField()
    lead_time = models.IntegerField()  # Lead time in days
    item_color = models.CharField(max_length=255)
    item_category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name

    class Meta:
        db_table = 'stock_item'

class SupplierStockItem(models.Model):
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    stock_item_id = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()


    class Meta:
        db_table = 'supplier_stock_item'
        unique_together = ('supplier_id', 'stock_item_id')    
