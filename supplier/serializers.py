from rest_framework import serializers
from .models import Supplier, SupplierCategory

class SupplierCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierCategory
        fields = ['supplier_category_id', 'supplier_category_name']

class SupplierSerializer(serializers.ModelSerializer):
    supplier_category = serializers.PrimaryKeyRelatedField(queryset=SupplierCategory.objects.all())

    class Meta:
        model = Supplier
        fields = [
            'supplier_id', 'supplier_name', 'registration_number', 'primary_contact_person',
            'address', 'mobile_number', 'email', 'bank_details', 'payment_terms',
            'country', 'shipping_port', 'shipping_terms', 'certification',
            'brands_work_with', 'supplier_category'
        ]