from django.shortcuts import render
from django.http import HttpRequest
from ecommerceapp.models import Contact,Products
from django.contrib import messages

def index(req:HttpRequest):
    all_products = Products.objects.all()
    return render(req, "index.html", {"products": all_products})




def contact_us(req:HttpRequest):
    username = req.POST.get("username")
    useremail = req.POST.get("email")
    desc = req.POST.get("description")
    phone_num = req.POST.get("phone_number")

    if not all([username,useremail,desc,phone_num]):
        return render(req,"pages/contact_us.html",{"contact_error_message": "Please fill in all fields."})
    
    Contact(name=username,email=useremail,desc=desc,phone_number=phone_num).save()

     
    return render(req,"pages/contact_us.html",{"contact_error_message":"We will contact soon!"})


def checkout(req:HttpRequest):
    return render(req,"pages/checkout.html")

def about_us(req:HttpRequest):
    return render(req,'pages/about_us.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')