from django import forms 
from .models import Product 

class ProductForm(forms.ModelForm):
    class Meta:
        # this code is used to create the form of the model
        model = Product 
        fields =['name','description', 'price','quantity','Availability']
        
