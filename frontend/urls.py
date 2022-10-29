from django.urls import path
from . import views


app_name = 'frontend'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('mysales/', views.mysales, name = 'mysales'),
    path('uploadnewproduct/', views.uploadproduct, name = 'upload'),
    path('details/<product_id>/', views.productdetails, name = 'details'),
    path('update/<product_id>/', views.updatepost, name = 'update'),
    path('delete/<product_id>/', views.deleteproduct, name = 'delete'),
]

# (r'^deal/(?P<post_id>[\w-]+)/$'