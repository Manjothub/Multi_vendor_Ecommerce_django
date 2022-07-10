from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import redirect, render
from . models import *
from django.contrib import messages
from cart.cart import Cart
from django.db.models import Max, Min, Sum
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

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
    return render(request,'registration/login.html')

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

@login_required(login_url='login')
def PROFILE(request):
    return render(request,'user/profile.html')


@login_required(login_url='login')
def PROFILEUPDATE(request):
    if request.method == 'POST':
        username= request.POST.get('user_name')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('user_password')
        user_id = request.user.id
        
        user = User.objects.get(id=user_id)
        user.first_name=first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        
        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request,"Profile Updated Sucessfully")
    return redirect('profile')

def ABOUTUS(request):
    return render(request,'user/about.html')

def CONTACTUS(request):
    return render(request,'user/contact.html')

def PRODUCTLIST(request):
    category = Category.objects.all()
    product = Product.objects.all()
    color = Color.objects.all()
    brands = Brand.objects.all()
    COLORID = request.GET.get('colorID')
    min_price = Product.objects.all().aggregate(Min('price'))
    max_price = Product.objects.all().aggregate(Max('price'))
    FilterPrice = request.GET.get('FilterPrice')
    if FilterPrice:
        Int_FilterPrice = int(FilterPrice)
        product = Product.objects.filter(price__lte = Int_FilterPrice)
    elif COLORID:
        product = Product.objects.filter(color = COLORID)
    else:
        product = Product.objects.all()
    context ={
        'category':category,
        'product':product,
        'min_price':min_price,
        'max_price':max_price,
        'FilterPrice':FilterPrice,
        'color':color,
        'brands':brands
    }
    return render(request,'user/product.html',context)

def FILTER_DATA(request):
     categories = request.GET.getlist('category[]')
     brands = request.GET.getlist('brand[]')
     allProducts = Product.objects.all().order_by('-id').distinct()
     if len(categories) > 0:
         allProducts = allProducts.filter(categories__id__in=categories).distinct()
     if len(brands) > 0:
        allProducts = allProducts.filter(brand__id__in=brands).distinct()
     t = render_to_string('Ajax/product-filtered-list.html', {'product': allProducts})
     return JsonResponse({'data': t})


def CART(request):
    return render(request,'user/cart.html')

@login_required(login_url="login")
def CART_ADD(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def ITEM_CLEAR(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="login")
def ITEM_INCREMENT(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def ITEM_DECREMENT(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="login")
def CART_DETAIL(request):
    cart = request.session.get('cart')
    pack_cost = sum(i['packing_cost'] for i in cart.values() if i)
    tax = sum(i['tax']for i in cart.values() if i)
    context={
    'pack_cost':pack_cost,
    'tax':tax,
        }
    return render(request, 'user/cart.html',context)









def LOGOUT(request):
    logout(request)
    return redirect ("/")