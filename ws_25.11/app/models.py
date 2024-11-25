from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Posts(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    description = models.TextField()
    likes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Posts)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


