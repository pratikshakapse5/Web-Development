from django import forms
from django.core import validators
from .models import Journal


class add_journal_form(forms.Form):
	Description= forms.CharField(max_length=100, label='Description')
	Entry= forms.CharField(max_length=100, label='Entry')

class edit_journal_form(forms.Form):
	Ids=forms.CharField(widget=forms.HiddenInput())
	Description=forms.CharField(max_length=100, label='Description')
	Entry=forms.CharField(max_length=200,widget=forms.Textarea)