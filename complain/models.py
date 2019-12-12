from django.db import models

# Create your models here.
class Complain(models.Model):
    Complain_id = models.AutoField(primary_key=True, max_length=5, blank=False, unique=True)
    Complain_type = models.CharField(max_length=55, blank=False)
    Complainant_name = models.CharField(max_length=55, blank=False)
    Mobile_Number = models.CharField(max_length=55, blank=False)
    District = models.CharField(max_length=55, blank=False)
    Thana = models.CharField(max_length=55, blank=False)
    Address = models.CharField(max_length=55, blank=False)
    Complain_description = models.CharField(max_length=55)
