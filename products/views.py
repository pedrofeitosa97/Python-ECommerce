from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from .models import Products
from .serializers import ProductsSerializer
from django.shortcuts import get_object_or_404
# Create your views here.

class ProductsView(APIView):
    def get(self, request: Request) -> Response:
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request: Request) -> Response:
        serializer = ProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class ProductsDetailView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        products = get_object_or_404(Products, pk=pk)
        serializer = ProductsSerializer(products)
        return Response(serializer.data, status.HTTP_200_OK)
    def patch(self, request: Request, pk: int) -> Response:
        products = get_object_or_404(Products, pk=pk)
        serializer = ProductsSerializer(products, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    def delete(self, request: Request, pk: int) -> Response:
        products = get_object_or_404(Products, pk=pk)
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    