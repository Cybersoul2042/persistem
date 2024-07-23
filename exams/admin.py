from django.contrib import admin
from .models import Exam


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['name','subject']
    search_fields = ['name','subject']
    ordering = ['name']
    prepopulated_fields = {"slug": ("name",)}
