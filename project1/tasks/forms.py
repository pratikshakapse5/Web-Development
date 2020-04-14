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

STATUS= [
	('Yes','Yes'),
	('No','No')
]

class add_task_form(forms.Form):
	Description= forms.CharField(max_length=100, label='Description')
	Category= forms.CharField(label='Category', widget=forms.Select(choices=CATEGORIES))

class edit_task_form(forms.Form):
	Ids=forms.CharField(widget=forms.HiddenInput())
	Completed=forms.ChoiceField(choices=STATUS)
	Description=forms.CharField(max_length=100, label='Description')
	Category=forms.CharField(label='Category', widget=forms.Select(choices=CATEGORIES))

class show_hine(forms.Form):
	 status=forms.BooleanField()
	 

   