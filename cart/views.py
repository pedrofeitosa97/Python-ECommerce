from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from .serializers import CartSerializer
from .models import Cart
from django.shortcuts import get_object_or_404

# Create your views here.
class CartView(APIView):
    def get(self, request: Request) -> Response:
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request: Request) -> Response:
        serializer = CartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    ...

class CartDetailView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        cart = get_object_or_404(Cart, pk=pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status.HTTP_200_OK)
    def patch(self, request: Request, pk: int) -> Response:
        cart = get_object_or_404(Cart, pk=pk)
        serializer = CartSerializer(cart, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    def delete(self, request: Request, pk: int) -> Response:
        carts = get_object_or_404(Cart, pk=pk)
        carts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)