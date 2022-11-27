from django.urls import path
from . import views


app_name = 'dashboard'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('details/<product_id>/', views.productdetails, name = 'details'),
]

# (r'^deal/(?P<post_id>[\w-]+)/$'