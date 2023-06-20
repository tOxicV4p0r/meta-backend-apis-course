from rest_framework import serializers
from decimal import Decimal
from .models import MenuItem,Booker,Category
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','slug','title']

class MenuItemSerializer(serializers.ModelSerializer):
# class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    def cal_tax(self, product:MenuItem):
        return product.price* Decimal(1.1) # 10%
    
    # stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='cal_tax')
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    # category = serializers.HyperlinkedRelatedField(
        # queryset = Category.objects.all(),
        # view_name='category-detail',
        ## serialized_item = MenuItemSerializer(items, many=True, context={'request': req})
    #)

    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory','price_after_tax','category','category_id']
        extra_kwargs = {
            'price': {'min_value': 2},
            'inventory':{'min_value':0}
        }
        # depth = 1

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booker
        fields = ['id','title','author','price']