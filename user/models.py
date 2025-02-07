from django.db import models

# Create your models here.
class ToDoList(models.Model):
    user = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    task = models.CharField(max_length=150)