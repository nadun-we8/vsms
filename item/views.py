from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import StockItem, ItemCategory, SupplierStockItem
from .serializers import StockItemSerializer, ItemCategorySerializer, SupplierStockItemSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def item_category_list(request):
    if request.method == 'GET':
        categories = ItemCategory.objects.all()
        serializer = ItemCategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ItemCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def item_category_detail(request, pk):
    try:
        category = ItemCategory.objects.get(pk=pk)
    except ItemCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemCategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ItemCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def stock_item_list(request):
    if request.method == 'GET':
        items = StockItem.objects.all()
        serializer = StockItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StockItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def stock_item_detail(request, pk):
    try:
        item = StockItem.objects.get(pk=pk)
    except StockItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StockItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StockItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def supplier_stock_item_list(request):
    if request.method == 'GET':
        items = SupplierStockItem.objects.all()
        serializer = SupplierStockItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SupplierStockItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def supplier_stock_item_detail(request, pk):
    try:
        item = SupplierStockItem.objects.get(pk=pk)
    except SupplierStockItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SupplierStockItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SupplierStockItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
