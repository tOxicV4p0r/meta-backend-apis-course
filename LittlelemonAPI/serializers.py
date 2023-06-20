from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import bleach
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
    
    #stock = serializers.IntegerField(source='inventory',min_value=0)
    #price = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=2)
    # price_after_tax = serializers.SerializerMethodField(method_name='cal_tax')
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    # category = serializers.HyperlinkedRelatedField(
        # queryset = Category.objects.all(),
        # view_name='category-detail',
        ## serialized_item = MenuItemSerializer(items, many=True, context={'request': req})
    #)

    """ 
    def validate_title(self, value):
        return bleach.clean(value) 
    """
    
    def validate(self, attrs):
        attrs['title'] = bleach.clean(attrs['title'])
        return super().validate(attrs)
    
    class Meta:
        model = MenuItem
        # fields = ['id','title','price','stock','price_after_tax','category','category_id']
        fields = ['id','title','price','inventory','category','category_id']
        extra_kwargs = {
            'price': {'min_value': 2},
            'inventory':{'min_value':0},
            # 'stock':{'source':'inventory','min_value':0},
            'title':{
                'validators':[
                    UniqueValidator(queryset=MenuItem.objects.all())
                ]
            }
        }
        # depth = 1

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booker
        fields = ['id','title','author','price']