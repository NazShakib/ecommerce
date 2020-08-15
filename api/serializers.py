from rest_framework import serializers
from store.models import Product, Customer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=['id','name','price']
        # fields ='__all__'


class ProductDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields='__all__'


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


