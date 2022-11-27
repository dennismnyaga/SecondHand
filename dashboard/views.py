from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from frontend.models import *
from users.models import *
from .forms import *

# Create your views here.

User = get_user_model()

def home(request):
    products = Product.objects.all()
    users = User.objects.all()

    verified_products = products.filter(status = True)
    verified_products_count = verified_products.count()
    unverified_products = products.filter(status = False)
    unverified_products_count = unverified_products.count()

    total_products = products.count()
    total_users = users.count()
    
    # print(verified_products_count)



    context = {'products':products, 'users':users, 'unverified_products_count':unverified_products_count, 'total_products':total_products, 'total_users':total_users, 'verified_products':verified_products, 'unverified_products':unverified_products, 'verified_products_count':verified_products_count}
    return render(request, 'dashboard/home.html', context)



def productdetails(request, product_id):
    user_credential = UserCredentials.objects.get(user = request.user)
    product = Product.objects.get(id=product_id)
    images = Photo.objects.filter(product=product)

    form = statusform(instance=product)
    if request.method == 'POST':
        form = statusform( request.POST ,instance=product)
        if form.is_valid():
            form.save()
            # instance = form.save(commit = False)
            # if Subcribers.objects.filter(email=instance.email).exists():
                # messages.warning(request, 'Email Already Exists!')
            # else:
            #     instance.save()
                # messages.success(request, 'Successfuly Subscribed')
            messages.success(request, 'Succesfully verified')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = statusform(instance=product)
    
    # bid_price = Bid.objects.filter(product=product).aggregate(Max('bid'))
    # bid_price = bid_pric.aggregate(Max('bid_pric'))
    # print(bid_price)
    # highest_bid_price = bid_price['bid__max']
    

    # if request.method == 'POST':
        
    #     user = request.user
    #     bid = request.POST['bid']
    #     product = product

    #     Bid.objects.create(
    #         user=user,
    #         bid=bid,
    #         product=product
    #     )
    #     messages.success(request, "Successfully bided on this product!")
    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        # return redirect('frontend:details', id=product_id)

    context = {'product': product, 'images':images, 'user_credential':user_credential, 'form':form}
    return render(request,'dashboard/details.html', context)
