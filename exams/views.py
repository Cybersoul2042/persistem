from django.shortcuts import render
from .models import Exam
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage, PageNotAnInteger

# Create your views here.


class ExamDetailView(DetailView):
    model = Exam
    template_name = "Examdetail.html"
    context_object_name = "Examdetail"


def Biology(request):
    exam = Exam.objects.filter(subject="Biology")
    pagee = request.GET.get("pagee", 1)
    paginator = Paginator(exam, 4)

    try:
        exams = paginator.page(pagee)
    except PageNotAnInteger:
        exams = paginator.page(1)
    except EmptyPage:
        exams = paginator.page(paginator.num_pages)

    return render(request, "Questions/Categories/Biology.html", {"exams": exams})


def Mathematics(request):
    exam = Exam.objects.filter(subject="Mathematics")
    page = request.GET.get("page", 1)
    paginator = Paginator(exam, 4)

    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        exams = paginator.page(1)
    except EmptyPage:
        exams = paginator.page(paginator.num_pages)

    return render(request, "Questions/Categories/Math.html", {"exams": exams})


def EBM(request):
    exam = Exam.objects.filter(subject="EBM")
    page = request.GET.get("page", 1)
    paginator = Paginator(exam, 4)

    try:
        exams = paginator.page(page)

    except PageNotAnInteger:

        exams = paginator.page(1)

    except EmptyPage:

        exams = paginator.page(paginator.num_pages)

    return render(request, "Questions/Categories/Ebm.html", {"exams": exams})


def Chemistry(request):
    exam = Exam.objects.filter(subject="Chemistry")
    page = request.GET.get("page", 1)
    paginator = Paginator(exam, 4)

    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        exams = paginator.page(1)
    except EmptyPage:
        exams = paginator.page(paginator.num_pages)

    return render(request, "Questions/Categories/Chemistry.html", {"exams": exams})
