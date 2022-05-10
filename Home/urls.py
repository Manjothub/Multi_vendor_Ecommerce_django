from django.urls import path
from Home .views import *

urlpatterns = [
    path('',INDEX,name="homepage"),
    path('product/<slug:slug>',PRDUCTDETAIL,name="product_detail"),
    path('error/',ERROR404,name="error404"),
    path('account/my-account',MYACCOUNT,name="myaccount"),
    path('account/register',REGISTER,name="register"),
    path('account/login',LOGIN,name="loginuser"),
    path( 'accounts/password_change/', name="password_change"),
    path( 'accounts/password_change/done/',name=" password_change_done"),
    path( 'accounts/password_reset/',name=" password_reset"),
    path( 'accounts/password_reset/done/',name=" password_reset_done"),
    path( 'accounts/reset/<uidb64>/<token>/',name=" password_reset_confirm"),
    path( 'accounts/reset/done/',name="password_reset_complete")
]