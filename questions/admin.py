from django.contrib import admin
from .models import Question

# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject',]
    search_fields = ['name','subject']
    ordering = ['name']