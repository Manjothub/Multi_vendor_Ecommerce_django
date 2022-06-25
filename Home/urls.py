from django.urls import path, include
from Home .views import *

urlpatterns = [
    path('',INDEX,name="homepage"),
    path('product/<slug:slug>',PRDUCTDETAIL,name="product_detail"),
    path('error/',ERROR404,name="error404"),
    path('account/my-account',MYACCOUNT,name="myaccount"),
    path('account/register',REGISTER,name="register"),
    path('account/login',LOGIN,name="loginuser"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile',PROFILE,name="profile"),
    path('accounts/profile/update',PROFILEUPDATE,name="profile_update"),
    path("logout/", LOGOUT, name="logout"),
    path("about-us",ABOUTUS,name="about-us"),
    path("contact-us",CONTACTUS,name="contact-us"),
    path("product",PRODUCTLIST,name="productlist"),
    path('products/filter-data',FILTER_DATA,name="filter-data"),
]