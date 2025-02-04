import uuid
from django.db import models

class SupplierCategory(models.Model):
    supplier_category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    supplier_category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.supplier_category_name

    class Meta:
        db_table = 'supplier_category'

class Supplier(models.Model):
    supplier_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    supplier_name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=255)
    primary_contact_person = models.CharField(max_length=255)
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    bank_details = models.TextField()
    payment_terms = models.TextField()
    country = models.CharField(max_length=255)
    shipping_port = models.CharField(max_length=255)
    shipping_terms = models.TextField()
    certification = models.TextField()
    brands_work_with = models.TextField()
    supplier_category = models.OneToOneField(SupplierCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.supplier_name

    class Meta:
        db_table = 'supplier'