from django.urls import path
from . import views

urlpatterns = [

       path('', views.home, name = "home"),
       path('contact/', views.contact, name = "contact"),
       path('books/', views.books, name = 'books'),
       path('profile/', views.profile, name = 'profile'),
       path('books/upload', views.upload_book, name = 'upload_book'),
       path('books/<int:pk>/', views.delete_book, name = 'delete_book'),

]