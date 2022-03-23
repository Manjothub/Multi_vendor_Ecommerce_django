from django.urls import path
from Home .views import *

urlpatterns = [
    path('',INDEX,name="homepage"),
    path('product/<slug:slug>',PRDUCTDETAIL,name="product_detail"),
    path('error/',ERROR404,name="error404")
]