from django.db import models
from mailbox import NoSuchMailboxError
# Create your models here.
class Familia(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    tlf=models.IntegerField()
    fechaNac=models.DateField()