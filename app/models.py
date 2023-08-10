from django.db import models

# Create your models here.
class Movie(models.Model):
    image=models.FileField(upload_to='photos/img',null=True,blank=True)
    name=models.CharField(max_length=20)
    desc=models.CharField(max_length=30)

    def __str__(self):
        return self.name
