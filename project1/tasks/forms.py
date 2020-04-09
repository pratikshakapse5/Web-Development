from django import forms
from django.core import validators
from .models import Task

CATEGORIES= [
    ('home','Home'),
    ('school', 'School'),
    ('work','Work'),
    ('self-employement','Self-employement'),
    ('other','Other'),
    ]

class add_task_form(forms.Form):
	Description= forms.CharField(max_length=100, label='Description')
	Category= forms.CharField(label='Category', widget=forms.Select(choices=CATEGORIES))

   