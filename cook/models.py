from django.core import files
from django.db import models
from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.deletion import CASCADE
# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    ingredients = models.TextField(null = True,blank=True)
    procedure = models.TextField(null = True,blank=True)
    link = models.TextField(null = True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['created']