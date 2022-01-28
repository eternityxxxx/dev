from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import login_view, logout_view, register_view

app_name = "authentication"

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register')
]
