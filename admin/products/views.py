from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import update
from .models import Product, User
from .producer import publish
from .serializers import ProductSerializer
import random

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        # add.apply_async((2, 1))
        serializer = ProductSerializer(products, many=True)
        # publish()
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # serializer=ProductSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # update.apply_async((pk,serializer.validated_data['title'],serializer.validated_data['image'],serializer.validated_data['likes']),countdown=10)
        publish('product_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        publish('product_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })