from django.shortcuts import render,redirect 
from .models import Product
from .forms import ProductForm 
from django.contrib import messages 


  
def products(request):
    
    items = Product.objects.all()
    products_count = items.count()
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid(): 
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.warning(request,f'{product_name} has been added ')
            return redirect('dashboard-products')
        
    else: 
        form =ProductForm() 
    context = {
        'items':items,
        'form':form,
        'products_count':products_count,
    } 
    return render(request,'dashboard/products.html',context)
 

def product_delete(request,pk):
    item=Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-products')
    return render(request,'dashboard/product_delete.html')
 
def product_update(request,pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else :
        form = ProductForm(instance=item)
    
    context={
        'form':form,
        
    }
    
    return render(request,'dashboard/product_update.html',context)
