from django.urls import path
from . import views

urlpatterns = [
       path('', views.authlogin, name = 'login'),
       path('register/', views.authregister, name = 'register'),
       #path('forgotpassword/', views.forgotpassword, name = 'forgotpassword'),
       path('logout/', views.authlogout, name = 'logout'),



       


       #path('contact/', views.contact, name = "contact"),
       #path('about/', views.about, name = "about"),
]