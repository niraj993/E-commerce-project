from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from configs.email_cred import EMAIL_SUBJECT
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
# from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode,force_bytes
# from django.contrib.auth.tokens import default_token_generator as generate_token
from django.contrib.auth import authenticate,login,logout


def signup(req:HttpRequest):
    if req.method=="POST":
        username = req.POST["username"]
        email = req.POST['email']
        password = req.POST['password']
        confirm_password = req.POST['confirm_password']

        if not all([username,email,password,confirm_password]):
            return render(req, "auth/signup.html", {"error_message": "Please fill in all fields."})
        
        if password != confirm_password:
            return render(req, "auth/signup.html", {"error_message": "Passwords do not match."})
        
        try:
            if User.objects.filter(email=email).exists():
                return render(req, "auth/signup.html", {"error_message": "You already have an account! Login Now"})

            user = User.objects.create_user(username=username,email=email,password=password)
            user.is_active = False
            user.save()
        
            # message = render_to_string("auth/email_template.html",{
            #     "user":user,
            #     "domain":"127.0.0.1:8001",
            #     "uid":urlsafe_base64_encode(force_bytes(user.pk)),
            #     "token":generate_token.make_token(user)
            # })

            messages.success(req, "Signed up successfully! Please login now.")

            return redirect(req, "auth/signin")

        except Exception as e:
            print(e)
            return render(req,"auth/signup.html",{"error_message":"Something went wrong! Try After some time"})
    return render(req,"auth/signup.html")




def signin(request:HttpRequest):
    if request.method == "POST":
        email = request.POST['useremail']
        password = request.POST['userpassword']

        if not all([email, password]):
            return render(request, "auth/signin.html", {"login_error_mess": "Please fill in all fields."})
        
        user = User.objects.filter(email=email).first()
        if user and user.check_password(password):
            login(request, user=user)  # Login the user here
            request.session.save()
            print(f"Session ID: {request.session.session_key}") 
            print(f"User {user.username} logged in.")
            print(f"Session: {request.session.items()}")
            print(f"Is user authenticated? {request.user.is_authenticated}")
            messages.success(request, "You have logged in successfully!")
            return redirect("/")  # Redirect to homepage after successful login
        
        return render(request, "auth/signin.html", {"login_error_mess": "Invalid credentials, please try again."})
    
    return render(request, "auth/signin.html")


        



  

def logout(req:HttpRequest):
    logout(req)
    messages.info(req,"Use has been ougout")
    return HttpResponse("asdfghjk")



def test_user(request):
    if request.user.is_authenticated:
        return HttpResponse(f"Authenticated user: {request.user.username}")
    else:
        return HttpResponse("You are not logged in.")

