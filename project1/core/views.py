from django.shortcuts import render, redirect
from core.forms import JoinForm, LoginForm

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from tasks.models import Task
from budget.models import Budget
from journal.models import Journal
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from core.models import UserProfileCore

def about(request):
	return render(request, 'core/about.html')

def home(request):
	if not request.user.is_authenticated:
		return render(request, 'core/login.html')
	else:
		task_list=Task.objects.select_related().filter(user=request.user)
		c_task=0
		p_task=0
		for line in task_list:
			if (line.completed=='No'):
				p_task=p_task+1
			else:
				c_task=c_task+1
		budget_list=Budget.objects.select_related().filter(user=request.user)
		journal_list=Journal.objects.select_related().filter(user=request.user)
		latest_date=Journal.objects.latest('date')
		today=datetime.now().date()
		diff=(today-latest_date.date)
		print(p_task)
		try:
			
			return render(request,'core/home.html',{'task_list':task_list,'completed':c_task,'pending':p_task, 'budget_list':budget_list,'journal_list':journal_list,'days':diff.days})
		#journal_list=Journal.objects.all
		except:
		
			return render(request,'core/home.html',{'task_list':task_list,'completed':c_task,'pending':p_task, 'budget_list':budget_list,'journal_list':journal_list,'days':diff.days})

def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            # Save form data to DB
            user = join_form.save()
            # Encrypt the password
            user.set_password(user.password)
            # Save encrypted password to DB
            user.save()
            # Success! Redirect to home page.
            return redirect("/")
        else:
            # Form invalid, print errors to console
            print(join_form.errors)
    else:
        join_form = JoinForm()
        page_data = { "join_form": join_form }
        return render(request, 'core/join.html', page_data)

def user_login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        print(request.POST)
        # First get the username and password supplied
        username = request.POST["username"]
        password = request.POST["password"]
        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)
		# If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to homepage
                return redirect("/home")
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
	
    else:
        #Nothing has been provided for username or password.
        return render(request, 'core/login.html', {})

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect("/")
