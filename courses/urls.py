from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('', views.course_list, name='class'),
    path('search/', views.searchcourses, name='searchcourses'),
]
