from django.db import models

# Create your models here.


class userregistration(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    password = models.CharField(max_length=10, blank=False)

