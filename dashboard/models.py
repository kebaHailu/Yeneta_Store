from django.db import models



# the following code will create a table in the database using orm concept 
class Product(models.Model):
    name = models.CharField(max_length=100,null=True)
    description = models.TextField(max_length=500,null=True)
    price = models.FloatField(null=False)
    quantity = models.PositiveIntegerField(null=True)
    Availability = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = 'Product'
    
    
    
    def __str__(self):
        return f'{self.name} - {self.quantity}' 
    
    
    
