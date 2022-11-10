from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
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
    context = {'product': product, 'images':images, 'more':more}

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
                current_bid = request.POST['current_bid'],
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
        if request.FILES.get('thumbnail') == None:
            thumbnail = images.product.thumbnail
            product_name = request.POST['product_name']
            price = request.POST['price']
            expected_sales_date = request.POST['expected_sales_date']
            description = request.POST['description']
            current_bid = request.POST['current_bid']
            category = Category.objects.get(id=request.POST['category']) # request.POST['category']

            photo = images.image

            
            
            
            # images.image = image
            # images.product.thumbnail = thumbnail
            # images.product.product_name = product_name
            # images.product.price = price
            # images.product.current_bid = current_bid
            # images.product.expected_sales_date = expected_sales_date
            # images.product.category = category
            # images.product.description = description

            # images.save()
            for image in images:
                product.save()
                image.save()

            # photo = Photo.objects.(
            #     product = product,
            #     image=image,
            # )

            
        
        if request.FILES.get('thumbnail') != None:
            thumbnail = images.product.thumbnail #request.FILES.get('thumbnail') 
            product_name = request.POST['product_name']
            price = request.POST['price']
            expected_sales_date = request.POST['expected_sales_date']
            description = request.POST['description']
            current_bid = request.POST['current_bid']
            category = Category.objects.get(id=request.POST['category']) # request.POST['category']
            photo = images.image
            # firstname = request.POST['first']
            # lastname = request.POST['last']
            # location = request.POST['location']
            # phone = request.POST['phone']
            # nationalno = request.POST['identitycardno']
            # idimage = user_credential.idimage

            images.image = image
            images.product.thumbnail = thumbnail
            images.product.product_name = product_name
            images.product.price = price
            images.product.current_bid = current_bid
            images.product.expected_sales_date = expected_sales_date
            images.product.category = category
            images.product.description = description

            images.save()

        if request.FILES.getlist('photo') == None:
            thumbnail = request.FILES.get('thumbnail') # images.product.thumbnail
            product_name = request.POST['product_name']
            price = request.POST['price']
            expected_sales_date = request.POST['expected_sales_date']
            description = request.POST['description']
            current_bid = request.POST['current_bid']
            category = Category.objects.get(id=request.POST['category']) # request.POST['category']
            photo = images.image


            # photo = images.image
            # idimage = user_credential.idimage
            # firstname = request.POST['first']
            # lastname = request.POST['last']
            # location = request.POST['location']
            # phone = request.POST['phone']
            # nationalno = request.POST['identitycardno']

            images.image = image
            images.product.thumbnail = thumbnail
            images.product.product_name = product_name
            images.product.price = price
            images.product.current_bid = current_bid
            images.product.expected_sales_date = expected_sales_date
            images.product.category = category
            images.product.description = description

            images.save()

        
        if request.FILES.get('photo') != None:
            thumbnail = request.FILES.getlist('photo')
            product_name = request.POST['product_name']
            price = request.POST['price']
            expected_sales_date = request.POST['expected_sales_date']
            description = request.POST['description']
            current_bid = request.POST['current_bid']
            category = Category.objects.get(id=request.POST['category']) # request.POST['category']
            photo = images.image

            images.image = image
            images.product.thumbnail = thumbnail
            images.product.product_name = product_name
            images.product.price = price
            images.product.current_bid = current_bid
            images.product.expected_sales_date = expected_sales_date
            images.product.category = category
            images.product.description = description

            images.save()

    context = {'images':images, 'product':product, 'categories':categories}
    return render(request, 'frontend/updatepost.html', context)



def addPhoto(request):
    return render(request, 'frontend/add.html')