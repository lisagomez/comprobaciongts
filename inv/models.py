from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Sucursal(models.Model):
    short_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    ceco = models.CharField(max_length=100)
    
    def __str__(self):
        return self.ceco

class ComprobacionGastos(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(default=timezone.now)
    sucursales = models.ManyToManyField(Sucursal)
    observations = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

