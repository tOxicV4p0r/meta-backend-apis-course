from django.contrib import admin
from .models import Book,MenuItem,Booker

# Register your models here.
admin.site.register(Book)
admin.site.register(MenuItem)
admin.site.register(Booker)