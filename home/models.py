from django.db import models

class students(models.Model):
    first_name = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    contact    = models.IntegerField()
    email      = models.EmailField(max_length=50)
    age        = models.IntegerField()
    # salery     = models.IntegerField()
    # services   = models.CharField(max_length=255)
    # phone      = models.CharField(max_length=12)








# Create your models here.
