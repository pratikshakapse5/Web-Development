from django.db import models

# Create your models here.

class Topic(models.Model):
	name = models.CharField(max_length=265, unique=True)

class Webpage(models.Model):
	category = models.ForeignKey(Topic, on_delete=models.CASCADE,)
	name = models.CharField(max_length=264)
	url = models.URLField()
