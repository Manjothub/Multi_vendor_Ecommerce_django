from django.shortcuts import redirect, render
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
    if products.exists():
        products = Product.objects.filter(slug = slug)
    else:
        return redirect('error404')
    context ={
            'products':products
    }
    return render(request,'user/product_detail.html',context)

def ERROR404(request):
    return render(request,'common/404.html')

def MYACCOUNT(request):
    return render(request,'main/login.html')