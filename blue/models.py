from django.db import models

# Create your models here.
class Blue(models.Model):
    title = models.CharField(max_length=1000)
    desc = models.TextField()

    def __str__(self):
        return super().__str__()