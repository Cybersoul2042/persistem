from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Exam(models.Model):
    SUBJECT_CHOICES = (
        ("biology", "Biology"),
        ("mathematics", "Mathematics"),
        ("ebm", "EBM"),
        ("chemistry", "Chemistry"),
    )

    subject = models.CharField(
        max_length=20, choices=SUBJECT_CHOICES, default="chemistry"
    )
    
    question = models.TextField()
    answer = models.TextField()
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, unique=True)

    def get_absolute_url(self):
        return reverse("Exam_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
