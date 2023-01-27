from django.db import models

# Create your models here.


#create a django model with name, location and status
class Client(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    status = models.BooleanField(default=True)