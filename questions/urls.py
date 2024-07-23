from django.urls import path
from . import views


urlpatterns = [
    path('your_question', views.QuestionFormView.as_view(), name='question_create'),
]
