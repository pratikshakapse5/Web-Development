from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
#    return redirect("home")

# Create your views here.
def home(request):
	return HttpResponse("Hello World!")
	