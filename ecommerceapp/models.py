from django.db import models
from django.contrib.auth.models import User
 

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    desc = models.TextField()  
    phone_number = models.CharField(max_length=15)   

    def __int__(self):
        return self.id


class Products(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100,default="")
    subcategory = models.CharField(max_length=100,default="")
    price = models.IntegerField(default=0)
    desc = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="images/images")

    def __int__(self):
        return self.id
    


class Cart(models.Model):
    """Cart model represents a user's cart in the e-commerce store."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    product = models.ForeignKey(Products, on_delete=models.CASCADE)   
    quantity = models.PositiveIntegerField(default=1)  
    added_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.product.product_name} - {self.quantity}"

    def get_total_price(self):
        """Calculates the total price for a product based on quantity."""
        return self.quantity * self.product.price
    
