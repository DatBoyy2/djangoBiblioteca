from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

app_name = "Users_app"
urlpatterns = [
    
    path('login/', LoginUser.as_view(), name='user-login'),
    path('logout/', LogoutUser.as_view(), name='user-logout'),
    path('register/', CreateUser.as_view(), name='user-create'),
    
]
