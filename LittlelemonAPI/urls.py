from django.urls import path
from . import views

urlpatterns = [
    # path('books', views.books),
    # path('books', views.BookList.as_view()),
    # path('books/<int:pk>', views.Book.as_view()),
    path('books', views.BooksView.as_view()),
    path('books/<int:pk>', views.SingleBookView.as_view()),

     path('menu-items', views.MenuItemsView.as_view()),
    # path('menu-items', views.menu_items,name='menu-detail'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),

    path('categories', views.CategoriesView.as_view()),
    # path('categories/<int:pk>', views.SingleCategoryView.as_view()),
    path('categories/<int:pk>', views.category_detail, name='category-detail'),
]