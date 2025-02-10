from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

# class EmailAuthBackend(BaseBackend):
#     def authenticate(self, req, email=None, password=None, **kwargs):
#         try:
#             user = User.objects.filter(email=email).first() 
#             if user and user.check_password(password):
#                 return user
#         except User.DoesNotExist:
#             return None
