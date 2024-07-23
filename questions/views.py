from .models import Question
from .forms import QuestionForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView

class QuestionCreateView(SuccessMessageMixin, CreateView):
    model = Question
    template_name = "Questions/Create.html"
    fields = ["name", "subject", "question", "answer"]
    success_url = reverse_lazy("home")
    success_message = "Your Question was created successfully"

class QuestionFormView(FormView):
    template_name = "Questions/Create.html"
    form_class = QuestionForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
