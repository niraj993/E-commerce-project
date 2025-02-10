from django.urls import path
from ecommerceapp import views
from configs.endpoints import CONTACT_US,ABOUT_US,DASHBOARD,CHECK_OUT,ADD_TO_CARD


urlpatterns = [
    path("",views.index,name="index"),
    path(DASHBOARD,views.dashboard),
    path(CONTACT_US,views.contact_us,name="contact-us"),
    path(ABOUT_US,views.about_us,name="about-us"),
    path(CHECK_OUT,views.checkout,name="checkout"),
    path(ADD_TO_CARD,views.add_to_cart,name="add_to_cart"),
    path('get_cart_count/', views.get_cart_count, name='get_cart_count'),
]
