from django.urls import path
from auth_app import views
from configs.endpoints import SIGN_UP,SIGN_IN,LOGOUT

urlpatterns = [
    path(SIGN_UP,views.signup,name="signup"),
    path(SIGN_IN,views.signin,name="signin"),
    path(LOGOUT,views.logout,name="logout"),
    path('test/', views.test_user, name='test_user')
]