from django.shortcuts import render
from . models import *

def INDEX(request):
    main_category = MainCategory.objects.all()
    product = Product.objects.filter(section__name = 'Top Deal of the Day')
    context ={
        'main_category':main_category,
        'products':product
    }
    return render(request,'user/index.html',context)

def PRDUCTDETAIL(request,slug):
    products = Product.objects.filter(slug = slug)
    context ={
        'products':products
    }
    return render(request,'user/product_detail.html',context)