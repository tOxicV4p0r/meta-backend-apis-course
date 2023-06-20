from django.shortcuts import render,get_object_or_404
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, EmptyPage

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes, throttle_classes
from django.contrib.auth.models import User, Group

from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttles import TenCallsPerMinute

# generics view
from rest_framework import generics
from .models import MenuItem,Book,Booker,Category,RatingUss
from .serializers import MenuItemSerializer,BookSerializer,CategorySerializer,RatingSerializer

# Create your views here.
# @csrf_exempt
# @api_view(['GET','POST','PUT']) # view in browser for debuging
# def books(req):
#    return Response('list of the books',status=status.HTTP_200_OK)

class BookList(APIView):
    def get(self,req):
        author = req.GET.get('author')
        if(author):
            return Response({"message":"List of the books by " + author})

        return Response({"message":"List of the books"},status.HTTP_200_OK)
    
    def post(self,req):
        return Response({"title":req.data.get("title")},status.HTTP_201_CREATED)

class Book(APIView):
    def get(self, req, pk):
        return Response({"message":"sigle book with id "+str(pk)}, status.HTTP_200_OK)
    
    def put(self, req, pk):
        return Response({"title":req.data.get("title")},status.HTTP_200_OK)

class BooksView(generics.ListCreateAPIView):
    queryset = Booker.objects.all()
    serializer_class = BookSerializer

class SingleBookView(generics.RetrieveUpdateAPIView):
    queryset = Booker.objects.all()
    serializer_class = BookSerializer

class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SingleCategoryView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuItemsView(generics.ListCreateAPIView):
    throttle_classes = [AnonRateThrottle,UserRateThrottle]
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer
    ordering_fields=['price','inventory']
    search_fields=['title','category__title']

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class RatingView(generics.ListCreateAPIView):
    queryset = RatingUss.objects.all()
    serializer_class = RatingSerializer

    def get_permissions(self):
        if(self.request.method == 'GET'):
            return []
        return [IsAuthenticated()]

@api_view(['GET'])
def rating_view(req):
    if( req.method == 'GET'):
        items = RatingUss.objects.all()
        serialized_item = RatingSerializer(items,many=True)
        return Response(serialized_item.data)
    
@api_view()
def category_detail(req, pk):
    category = get_object_or_404(Category,pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data, status.HTTP_200_OK) 

@api_view(['GET','POST'])
def menu_items(req):
    if( req.method == 'GET'):
        items = MenuItem.objects.select_related('category').all()

        category_name = req.query_params.get('category')
        to_price = req.query_params.get('to_price')
        search = req.query_params.get('search')
        ordering = req.query_params.get('ordering')
        perpage = req.query_params.get('perpage',default=2)
        page = req.query_params.get('page',default=1)

        if category_name:
            items = items.filter(category__title = category_name)
        if to_price:
            items = items.filter(price = to_price)
        if search:
            items = items.filter(tittle__contains = search)
        if ordering:
            ordering_fields = ordering.split(",")
            items = items.order_by(*ordering_fields)

        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []

        serialized_item = MenuItemSerializer(items,many=True)
        return Response(serialized_item.data)

    if( req.method == 'POST'):
        serialized_item = MenuItemSerializer(data=req.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)

@api_view()
@permission_classes([IsAuthenticated])
def secret(req):
    return Response({"message":"Some secret message"})


@api_view()
@permission_classes([IsAuthenticated])
def manager_view(req):
    if req.user.groups.filter(name='Manager').exists():
        return Response({"message":"Only Manager Should see"})
    else:
        return Response({"message":"You are not authorized"},403)

@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(req):
    return Response({"message":"successful"})

@api_view()
@permission_classes([IsAuthenticated])
# @throttle_classes([UserRateThrottle])
@throttle_classes([TenCallsPerMinute])
def throttle_check_auth(req):
    return Response({"message":"logged in users only"})

@api_view(['POST','DELETE'])
@permission_classes([IsAdminUser])
def manager(req):
    username = req.POST.get('username')
    if username:
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name="Manager")
        if req.method =='POST':
            managers.user_set.add(user)
            return Response({"message":"add ok"})
        elif req.method == 'DELETE':
            managers.user_set.remove(user)
            return Response({"message":"delete ok"})

    return Response({"message":"error"}, status.HTTP_400_BAD_REQUEST)

""" 
def books(req):
    if(req.method == 'GET'):
        books = Book.objects.all().values()
        return JsonResponse({"books":list(books)})
    elif req.method == 'POST':
        title = req.POST.get('title')
        author = req.POST.get('author')
        price = req.POST.get('price')
        book = Book(
            title = title,
            author = author,
            price = price
        )

        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status = 400)
        return JsonResponse(model_to_dict(book),status = 201)
 """

