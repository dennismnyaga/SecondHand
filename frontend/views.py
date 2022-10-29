from django.shortcuts import render, redirect
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

    product = Product.objects.order_by('-date_posted')
    bids = Bid.objects.order_by('-timestamp')
    paginator = Paginator(product, 5)
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
    products = Product.objects.filter(poster=request.user).order_by('-date_posted')
    context = {"products":products}
    return render(request, 'frontend/mysales.html', context)



def productdetails(request, product_id):
    more = Product.objects.order_by('-date_posted')[0:10]
    product = Product.objects.get(id=product_id)
    context = {'product': product, 'more':more}

    return render(request,'frontend/details.html', context)

def updatepost(request, product_id):

    product = Product.objects.get(id=product_id)
    form = updateform(instance=product)
    if request.method == 'POST':
        form = updateform(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('/')
    context = {'form': form, 'product':product}
    return render(request, 'frontend/updatepost.html', context)


@login_required(login_url='users:signin')
def uploadproduct(request):
    categories = Category.objects.all()
    user_credential = UserCredentials.objects.get(user = request.user)
    if request.method == 'POST':
        poster = request.user
        images = request.FILES.get('images')
        product_name = request.POST['product_name']
        price = request.POST['price']
        if request.POST['category'] != 'none':
            category = Category.objects.get(id=request.POST['category'])
        # elif request.POST['category_new'] != '':
        #     category, created = Category.objects.get_or_create(
        #         user=user,
        #         name=data['category_new'])
        else:
            category = None
        # category = request.POST['category']
        expected_sales_date = request.POST['expected_sales_date']
        current_bid = request.POST['current_bid']
        details = request.POST['details']



        # user_credential.user_image = image
        # user_credential.idimage = idimage
        # user_credential.first_name = firstname
        # user_credential.last_name = lastname
        # user_credential.phone = phone
        # user_credential.nationalno = nationalno
        # user_credential.location = location

       
        for image in images:
            Product.objects.create(
                poster=poster,
                images=images,
                product_name=product_name,
                price=price,
                category=category,
                expected_sales_date=expected_sales_date,
                current_bid=current_bid,
                details=details,
            )
            return redirect('/')
    context = {'categories':categories}
    return render(request, 'frontend/upload.html', context)


def deleteproduct(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method =='POST':
        product.delete()
        return redirect('/')
    context = {'product':product}
    return render(request, 'frontend/delete.html', context)

def placebid(request):
    pass