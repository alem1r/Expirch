
from rest_framework import serializers
from .models import Product, Email

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'nameFile']

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Email
        fields = ['email']