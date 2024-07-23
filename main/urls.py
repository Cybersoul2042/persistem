from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
]
