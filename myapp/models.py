from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return super().__str__()


class Todo(models.Model):
    title = models.CharField(max_length=1000)
    desc = models.TextField()

    def __str__(self):
        return super().__str__()

class Blog(models.Model):
    title = models.CharField(max_length=1000)
    desc = models.TextField()

    def __str__(self):
        return super().__str__()