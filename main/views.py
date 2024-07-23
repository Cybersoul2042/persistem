from django.views.generic import ListView
from courses.models import Course


class HomePage(ListView):
    model= Course
    template_name='index.html'
    context_object_name= 'newc'
    def get_queryset(self) :
        return self.model.objects.order_by('-id')[:3]
