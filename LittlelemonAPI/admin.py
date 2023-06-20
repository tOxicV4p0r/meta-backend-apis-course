from django.contrib import admin
from .models import Book,MenuItem,Booker,Category,RatingUss

# Register your models here.
admin.site.register(Book)
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Booker)
admin.site.register(RatingUss)