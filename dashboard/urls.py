from django.urls import path
from . import views 

# the following code will create the url for the dashboard app
urlpatterns = [
    
    path('products/',views.products, name='dashboard-products'),
    path('products/delete/<int:pk>/',views.product_delete, name='dashboard-product-delete'),
    path('products/update/<int:pk>/',views.product_update, name='dashboard-product-update'),
]