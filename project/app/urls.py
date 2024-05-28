from django.urls import path
from .views import *
urlpatterns=[
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('showdata/',showdata,name='showdata'),
    path('addTocart/<int:pk>',addTocart,name='addTocart'),
    path('addTocart/',cart,name='cart'),
]