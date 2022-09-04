from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    year_of_birth = models.IntegerField()
    country = models.CharField(max_length=50)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
