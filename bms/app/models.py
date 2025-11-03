from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Poster(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doc=models.FileField(upload_to='uploads/')
    
    def __str__(self):
        return str(self.doc)