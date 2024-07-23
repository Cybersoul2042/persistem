from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login_view, name='login'),
    path('', views.logout, name='logout'),
    path('register', views.register_view, name='register')
]