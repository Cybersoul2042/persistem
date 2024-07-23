from django.urls import path
from . import views

urlpatterns = [
    path('Questionbank/<slug:slug>/', views.ExamDetailView.as_view(), name='Examdetail'),
    path('Questionbank/Biology', views.Biology, name='Biology_page'),
    path('Questionbank/Chemistry', views.Chemistry, name='chemistry_page'),
    path('Questionbank/EBM', views.EBM, name='EBM_page'),
    path('Questionbank/Mathematics', views.Mathematics, name='mathematics_page')
]
