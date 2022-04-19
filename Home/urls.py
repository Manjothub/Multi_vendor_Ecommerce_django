from django.urls import path
from Home .views import *

urlpatterns = [
    path('',INDEX,name="homepage"),
    path('product/<slug:slug>',PRDUCTDETAIL,name="product_detail"),
    path('error/',ERROR404,name="error404"),
    path('account/my-account',MYACCOUNT,name="myaccount"),
    path('account/register',REGISTER,name="register"),
    path('account/login',LOGIN,name="loginuser"),
]