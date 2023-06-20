from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.views import APIView

# generics view
from rest_framework import generics
from .models import MenuItem,Book,Booker
from .serializers import MenuItemSerializer,BookSerializer

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

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


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