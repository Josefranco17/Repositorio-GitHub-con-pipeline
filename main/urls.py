from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('nuevo/', views.book_create, name='book_create'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('<int:pk>/editar/', views.book_update, name='book_update'),
    path('<int:pk>/eliminar/', views.book_delete, name='book_delete'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:pk>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:pk>/', views.cart_remove, name='cart_remove'),
    path('cart/clear/', views.cart_clear, name='cart_clear'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
