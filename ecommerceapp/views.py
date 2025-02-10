from django.shortcuts import render
from django.http import HttpRequest
from ecommerceapp.models import Contact,Products,Cart
from django.http import JsonResponse
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



def add_to_cart(request, product_id):
    """Adds a product to the cart and returns the updated cart item count."""
    # if not request.user.is_authenticated:
    #     return JsonResponse({'error': 'User not authenticated'}, status=400)

    product = Products.objects.get(id=product_id)
    user = request.user
    cart_item, created = Cart.objects.get_or_create(user=user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    cart_count = Cart.objects.filter(user=user).count()
    return JsonResponse({'cart_count': cart_count})



def get_cart_count(request):
    """Get the current cart count for the logged-in user."""
    # if not request.user.is_authenticated:
    #     return JsonResponse({'cart_count': 0})  

    user = request.user
    cart_count = Cart.objects.filter(user=user).count()
    return JsonResponse({'cart_count': cart_count})




def checkout(req:HttpRequest):
    return render(req,"pages/checkout.html")

def about_us(req:HttpRequest):
    return render(req,'pages/about_us.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')