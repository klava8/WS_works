from django.db import models
from django.db.models.fields import *

# Create your models here.
class Posts(models.Model):
    image = TextField()
    title = CharField(max_length=80)
    description = TextField()
    comments = TextField()
    likes = IntegerField()