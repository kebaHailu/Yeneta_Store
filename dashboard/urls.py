from django.urls import path
from . import views 

# the following code will create the url for the dashboard app
urlpatterns = [
    
    path('',views.products, name='dashboard-products'),
    path('delete/<int:pk>/',views.product_delete, name='dashboard-product-delete'),
    path('update/<int:pk>/',views.product_update, name='dashboard-product-update'),
]