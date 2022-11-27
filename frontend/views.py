from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.db.models import Max
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth

from .models import *
from users.models import UserCredentials
from .forms import *




def home(request):
    # user_object = User.objects.get(username = request.user.username)
    # user_credentials = UserCredentials.objects.get(user = user_object)


    product = Product.objects.order_by('-timestamp')
    paginator = Paginator(product, 21)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    context = {"products":products}
    return render(request, 'frontend/home.html', context)

def comments(request):
    username = request.user.username
    bid_id = request.GET.get('bid_id')

    product = Product.objects.get(id = bid)
    comment_filter = Bid.objects.filter(bid_id=bid_id, username = username).first()

def mysales(request):
    products = Product.objects.filter(poster=request.user)
    context = {"products":products}
    return render(request, 'frontend/mysales.html', context)



def productdetails(request, product_id):
    more = Product.objects.order_by('-timestamp')
    product = Product.objects.get(id=product_id)
    images = Photo.objects.filter(product=product)
    bid_price = Bid.objects.filter(product=product).aggregate(Max('bid'))
    # bid_price = bid_pric.aggregate(Max('bid_pric'))
    # print(bid_price)
    highest_bid_price = bid_price['bid__max']
    

    if request.method == 'POST':
        
        user = request.user
        bid = request.POST['bid']
        product = product

        

        Bid.objects.create(
            user=user,
            bid=bid,
            product=product
        )
        messages.success(request, "Successfully bided on this product!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        # return redirect('frontend:details', id=product_id)
    # else:
    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    context = {'product': product, 'images':images, 'more':more, 'bid_price':bid_price ,'highest_bid_price':highest_bid_price}
    return render(request,'frontend/details.html', context)


   




    

def deleteproduct(request, product_id):
    product = Product.objects.get(id=product_id)
    images = Photo.objects.filter(product=product)
    if request.method =='POST':
        product.delete()
        images.delete()
        return redirect('/')
    context = {'product':product}
    return render(request, 'frontend/delete.html', context)

def placebid(request):
    pass


def vehecles(request):
    product = Product.objects.filter(category__name='Vehicles')

    paginator = Paginator(product, 21)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
  
    context = {'products':products}
    return render(request, 'frontend/vehecles.html', context)


def electronics(request):
    product = Product.objects.filter(category__name='Mobile Phones, Tablets, & Accessories')

    paginator = Paginator(product, 21)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
  
    context = {'products':products}
    return render(request, 'frontend/electronics.html', context)


def generalelectronics(request):
    product = Product.objects.filter(category__name='Electronics & Home Appliances')

    paginator = Paginator(product, 21)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
  
    context = {'products':products}
    return render(request, 'frontend/generalelectronics.html', context)


def fashion(request):
    product = Product.objects.filter(category__name='Fashion and Beauty')

    paginator = Paginator(product, 21)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
  
    context = {'products':products}
    return render(request, 'frontend/fashion.html', context)



def furniture(request):
    product = Product.objects.filter(category__name='Home Furniture & Decor')

    paginator = Paginator(product, 21)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
  
    context = {'products':products}
    return render(request, 'frontend/furniture.html', context)



def properties(request):
    product = Product.objects.filter(category__name='Properties')

    paginator = Paginator(product, 21)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
  
    context = {'products':products}
    return render(request, 'frontend/properties.html', context)


def more(request):
    product = Product.objects.filter(category__name='Others')

    paginator = Paginator(product, 21)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
  
    context = {'products':products}
    return render(request, 'frontend/more.html', context)




def individual(request):
    return render(request, 'frontend/individual.html')




@login_required(login_url='users:signin')
def uploadproduct(request):
  

    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None
        # ===================================
        product, created = Product.objects.get_or_create(
                poster=request.user,
                product_name = request.POST['product_name'],
                thumbnail = request.FILES.get('thumbnail'),
                price = request.POST['price'],
                description=request.POST['description'],
                category = Category.objects.get(id=request.POST['category']),
                expected_sales_date = request.POST['expected_sales_date'],
                
            )
        # ===================================

        for image in images:
            photo = Photo.objects.create(
                product = product,
                image=image,
            )

        return redirect('/')

    context = {'categories': categories}
    return render(request, 'frontend/upload.html', context)


def updatepost(request, product_id):
    categories = Category.objects.all()
    product = Product.objects.get(id=product_id)
    images = Photo.objects.filter(product=product)
    if request.method == 'POST':
        # ==========================================
        if request.FILES.getlist('photo') == None:
            product_name = request.POST['product_name']
            price = request.POST['price']
            expected_sales_date = request.POST['expected_sales_date']
            description = request.POST['description']
            category = Category.objects.get(id=request.POST['category']) # request.POST['category']
            photo = images.image



            images.image = image
            images.product.product_name = product_name
            images.product.price = price
            images.product.expected_sales_date = expected_sales_date
            images.product.category = category
            images.product.description = description
            images.save()

        
        if request.FILES.get('photo') != None:
            product_name = request.POST['product_name']
            price = request.POST['price']
            expected_sales_date = request.POST['expected_sales_date']
            description = request.POST['description']
            category = Category.objects.get(id=request.POST['category'])
            photo = images.image

            images.image = image
           
            images.product.product_name = product_name
            images.product.price = price
           
            images.product.expected_sales_date = expected_sales_date
            images.product.category = category
            images.product.description = description

            images.save()

    context = {'images':images, 'product':product, 'categories':categories}
    return render(request, 'frontend/updatepost.html', context)



def addPhoto(request):
    return render(request, 'frontend/add.html')