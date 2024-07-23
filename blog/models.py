from django.db import models

# Create your models here.

class Post(models.Model):
     title = models.CharField(max_length=200)
     slug = models.SlugField(allow_unicode=True)
     caption = models.TextField()
     thumbnail = models.ImageField(upload_to="post_thumbnails", null=True, blank=True)
     author = models.CharField(max_length=200, null=True, blank=True)

     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)