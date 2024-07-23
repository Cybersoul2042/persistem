from django.db import models

# Create your models here.


class Question(models.Model):
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

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
