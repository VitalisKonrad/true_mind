from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class MindPost(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mind_posts') # change om auth.User when create uathentication
    body = models.CharField(max_length=170)
    created = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        ordering = ('-created',)