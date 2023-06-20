from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

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

    path('secret/', views.secret),
    path('api-token-auth/', obtain_auth_token),
    path('manager-view/',views.manager_view),
    path('throttle-check/',views.throttle_check),
    path('throttle-check-auth/',views.throttle_check_auth),

    path('groups/manager/users',views.manager),
    
    # path('ratings',views.rating_view),
    path('ratings',views.RatingView.as_view()),
]