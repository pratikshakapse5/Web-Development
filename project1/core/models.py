from django.db import models
from django.contrib.auth.models import User


class UserProfileCore(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	tasks_view_hide_flag=models.BooleanField(default=False)

def __str__(self):
	return self.user.username
	
