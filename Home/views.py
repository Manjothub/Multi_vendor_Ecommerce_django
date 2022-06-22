from django.shortcuts import redirect, render
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
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
    return render(request,'registeration/login.html')

def REGISTER(request):
    if request.method =='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('cpassword')
        if User.objects.filter(username=username).exists():
            messages.error(request,'username is already exists')
            return redirect ('login')   
        if User.objects.filter(email=email).exists():
            messages.error(request,'Sorry email already exists')
            return redirect ('login') 
        else:
            if password==confirm_password:
             user = User(username=username,email= email)
             user.set_password(password)
             user.save()
             messages.success(request,'Account Created Sucessfully')
            else:
                messages.error(request,'Password not Matched')
    return redirect('myaccount')

def LOGIN(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Sucessfully')
            return redirect('homepage')
        else:
            messages.error(request,'Invalid Credentials!!')
            return redirect('myaccount')
    return render(request,'registeration/login.html')