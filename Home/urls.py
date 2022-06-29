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
    path('cart/add/<int:id>/', CART_ADD, name='cart_add'),
    path('cart/item_clear/<int:id>/', ITEM_CLEAR, name='item_clear'),
    path('cart/item_increment/<int:id>/',ITEM_INCREMENT, name='item_increment'),
    path('cart/item_decrement/<int:id>/',ITEM_DECREMENT, name='item_decrement'),
    path('cart/cart_clear/', ITEM_CLEAR, name='cart_clear'),
    path('cart/cart-detail/',CART_DETAIL,name='cart_detail'),
]