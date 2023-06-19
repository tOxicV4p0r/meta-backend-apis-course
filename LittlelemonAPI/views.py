from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Book

# Create your views here.
@csrf_exempt
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
