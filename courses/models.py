from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    published = models.DateTimeField()
    img = models.ImageField(null=True, blank=True)
    img2 = models.ImageField(null=True, blank=True)
    doc = models.TextField()
    link = models.URLField(null=True, blank=True)
    mr1 = models.CharField(max_length=50)
    mr2 = models.CharField(max_length=50, blank=True)
    mr3 = models.CharField(max_length=50, blank=True)
    mr4 = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(null=True, unique=True)

    def get_absolute_url(self):
        return reverse("course_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
