from rest_framework import serializers
from .models import MenuItem,Booker

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booker
        fields = ['id','title','author','price']