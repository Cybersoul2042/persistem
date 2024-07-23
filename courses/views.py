from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Course
from django.urls import reverse_lazy
from django.views.generic import DetailView

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage, PageNotAnInteger


class CourseDetailView(DetailView):
    model = Course
    template_name = "detail.html"
    context_object_name = "detail"


def course_list(request):
    courses = Course.objects.all()
    page = request.GET.get("page", 1)
    paginator = Paginator(courses, 9)
    try:
        classes = paginator.page(page)
    except PageNotAnInteger:
        classes = paginator.page(1)
    except EmptyPage:
        classes = paginator.page(paginator.num_pages)
    return render(request, "Courses/index.html", {"classes": classes})


def searchcourses(request):
    if request.method == "POST":
        q = request.POST["q"]
        searched = Course.objects.filter(name__contains=q)
        return render(request, "searchcourses.html", {"q": q, "searched": searched})
    else:
        return render(request, "index.html")
