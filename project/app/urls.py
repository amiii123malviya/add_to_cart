from django.urls import path
from .views import *
urlpatterns=[
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('showdata/',showdata,name='showdata'),
    path('addTocart/<int:pk>',addTocart,name='addTocart'),
    path('cart/',cart,name='cart'),
    path('delete/<int:pk>',delete,name='delete'),
]