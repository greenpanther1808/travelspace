from django.db import models

# Create your models here.
class struct(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    descr=models.TextField()
    def __str__(self):
        return self.name
class team(models.Model):
    names=models.CharField(max_length=250)
    imag=models.ImageField(upload_to='imgs')
    teamdescr=models.TextField()
    def __str__(self):
        return self.names
