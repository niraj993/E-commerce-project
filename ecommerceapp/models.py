from django.db import models

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
    
