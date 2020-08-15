from django.shortcuts import render
from django.http import JsonResponse
import json


from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .serializers import ProductSerializer, ProductDetailSerializers, CustomerSerializers
from store.models import Product, Customer


@api_view(['GET'])
@authentication_classes([SessionAuthentication,BasicAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def product_list(request):
    product = Product.objects.all().order_by('-id')
    serializer = ProductSerializer(product,many= True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication,BasicAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def product_details(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductDetailSerializers(product,many=False)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication,BasicAuthentication])
@permission_classes([IsAuthenticated])
def product_update(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductDetailSerializers(instance=product,data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response('Item Updated Successfully')


@api_view(['POST'])
@authentication_classes([SessionAuthentication,BasicAuthentication])
@permission_classes([IsAdminUser])
def product_create(request):
    serializer = ProductDetailSerializers(data= request.data)
    if serializer.is_valid():
        serializer.save()

    return Response('Item Added Successfully')


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication,BasicAuthentication])
@permission_classes([IsAdminUser])
def product_delete(request,pk):
    product = Product.objects.get(id=pk)
    imag = product.product_image
    product.delete()
    imag.delete(save=False)
    return Response('Item Deleted Successfully')


#customer details showing 
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def customer_Details(request):
    customer = Customer.objects.all().order_by('-id')
    serializer = CustomerSerializers(customer, many= True)
    return Response(serializer.data)


def testing(request):
    responseData = {
        'product-list': 'localhost:8000/api/product-list',
        'product-details': 'localhost:8000/api/product-detail/1',
        'product-create': 'localhost:8000/api/product-create',
        'product-update': 'localhost:8000/api/product-update/2',
        'product-delete': 'localhost:8000/api/product-delete/3',
        'customer-details': 'localhost:8000/api/customer-details',
        'roles' : ['Admin','User']
    }
    return JsonResponse(responseData)


