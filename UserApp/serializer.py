from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from UserApp.models import Product, Cart


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'quantity']

