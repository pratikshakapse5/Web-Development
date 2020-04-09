from django.db import models

# Create your models here.

Categories = (
    ('home','Home'),
    ('school', 'School'),
    ('work','Work'),
    ('self-employement','Self-employement'),
    ('other','Other'),
)

class Task(models.Model):
	category = models.CharField(max_length=6, choices=Categories, default='other')
	description= models.CharField(max_length=100)
	completed=models.CharField(max_length=10,default="No")