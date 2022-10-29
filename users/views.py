from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import UserCredentials
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken!')
                return redirect('users:signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken!')
                return redirect('users:signup')
            else:
                user = User.objects.create_user(username = username, email = email, password = password)
        
                user.save()
                # log user in and redirect to settings page.
                user_login = auth.authenticate(username = username, password = password)
                auth.login(request, user_login)

                #  create a profile object for the new user

                user_model = User.objects.get(username = username)
                new_profile = UserCredentials.objects.create(user = user_model, id_user = user_model.id)
                new_profile.save()
                return redirect('users:usercredentials')
        else:

            messages.info(request, 'Passwords not martching!')
            return redirect('users:signup')
    else:
        return render(request, 'users/signup.html')



def signin(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('frontend:home')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('users:signin')
    return render(request, 'users/signin.html')



@login_required(login_url='users:signin')
def logout(request):
    auth.logout(request)
    return redirect('users:signin')

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form. 
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('frontend:home')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)



def credentials(request):
    user_credential = UserCredentials.objects.get(user = request.user)

    if request.method == 'POST':
        if request.FILES.get('image') == None:
            image = user_credential.user_image
            firstname = request.POST['first']
            lastname = request.POST['last']
            location = request.POST['location']
            phone = request.POST['phone']
            nationalno = request.POST['identitycardno']
            idimage = user_credential.idimage


            user_credential.user_image = image
            user_credential.idimage = idimage
            user_credential.first_name = firstname
            user_credential.last_name = lastname
            user_credential.phone = phone
            user_credential.nationalno = nationalno
            user_credential.location = location
            user_credential.save()
        
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            firstname = request.POST['first']
            lastname = request.POST['last']
            location = request.POST['location']
            phone = request.POST['phone']
            nationalno = request.POST['identitycardno']
            idimage = user_credential.idimage

            user_credential.user_image = image
            user_credential.idimage = idimage
            user_credential.first_name = firstname
            user_credential.last_name = lastname
            user_credential.phone = phone
            user_credential.nationalno = nationalno
            user_credential.location = location
            user_credential.save()

        if request.FILES.get('id_pic') == None:
            image = user_credential.user_image
            idimage = user_credential.idimage
            firstname = request.POST['first']
            lastname = request.POST['last']
            location = request.POST['location']
            phone = request.POST['phone']
            nationalno = request.POST['identitycardno']

            user_credential.user_image = image
            user_credential.idimage = idimage
            user_credential.first_name = firstname
            user_credential.last_name = lastname
            user_credential.phone = phone
            user_credential.nationalno = nationalno
            user_credential.location = location
            user_credential.save()
        
        if request.FILES.get('id_pic') != None:
            idimage = request.FILES.get('id_pic')
            firstname = request.POST['first']
            lastname = request.POST['last']
            location = request.POST['location']
            phone = request.POST['phone']
            nationalno = request.POST['identitycardno']
            image = user_credential.user_image

            user_credential.user_image = image
            user_credential.idimage = idimage
            user_credential.first_name = firstname
            user_credential.last_name = lastname
            user_credential.phone = phone
            user_credential.nationalno = nationalno
            user_credential.location = location
            user_credential.save()
        
        return redirect('users:usercredentials')
    return render(request, 'users/usercredentials.html', {'user_credential':user_credential})