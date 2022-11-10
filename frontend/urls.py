from django.urls import path
from . import views


app_name = 'frontend'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('mysales/', views.mysales, name = 'mysales'),


    path('vehecles/', views.vehecles, name = 'vehecles'),
    path('electronics/', views.electronics, name = 'electronics'),
    path('fashion/', views.fashion, name = 'fashion'),
    path('furniture/', views.furniture, name = 'furniture'),
    path('more/', views.more, name = 'more'),
    path('properties/', views.properties, name = 'properties'),
    path('generalelectronics/', views.generalelectronics, name = 'general'),


    path('uploadnewproduct/', views.uploadproduct, name = 'upload'),
    path('details/<product_id>/', views.productdetails, name = 'details'),
    path('update/<product_id>/', views.updatepost, name = 'update'),
    path('delete/<product_id>/', views.deleteproduct, name = 'delete'),
    



     path('ind/', views.individual),


    path('add/', views.addPhoto, name='add'),
    
]

# (r'^deal/(?P<post_id>[\w-]+)/$'