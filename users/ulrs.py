from django.urls import path, include
from .import views

app_name = 'users'

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('usercredentials/', views.credentials, name='usercredentials'),
]