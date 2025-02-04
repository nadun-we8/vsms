from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import VirtualStock
from .serializers import VirtualStockSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def virtual_stock_list(request):
    if request.method == 'GET':
        stocks = VirtualStock.objects.all()
        serializer = VirtualStockSerializer(stocks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VirtualStockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def virtual_stock_detail(request, pk):
    try:
        stock = VirtualStock.objects.get(pk=pk)
    except VirtualStock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VirtualStockSerializer(stock)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VirtualStockSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
