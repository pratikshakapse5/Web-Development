from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Journal(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	date = models.DateField(auto_now=True)
	description= models.CharField(max_length=100)
	entry=models.CharField(max_length=100)