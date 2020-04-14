from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from tasks.models import Task
from tasks.forms import add_task_form, edit_task_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from core.models import UserProfileCore

# Create your views here.
@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
#    return redirect("home")
def tasks(request):
	if not request.user.is_authenticated:
		return render(request, 'core/login.html')
	else:
		if request.method == 'POST':
			t_form = edit_task_form(request.POST)
			if(t_form.is_valid()):
				task_list_data = Task.objects.get(id=t_form.cleaned_data["Ids"])
				task_list_data.description = t_form.cleaned_data["Description"]
				task_list_data.category = t_form.cleaned_data["Category"]
				task_list_data.completed = t_form.cleaned_data["Completed"]
				task_list_data.save()
		
		tasks_obj = Task.objects.select_related().filter(user=request.user)
		return render(request, 'tasks/view_task_list.html', {"alltasks": tasks_obj} )

#@login_required(login_url='/login/')
def add_task(request):
		if (request.method == 'POST'):
			form = add_task_form(request.POST);
			if (form.is_valid()):
				#user=user.request
				Description = form.cleaned_data['Description']  #names on the left are from form
				Category = form.cleaned_data['Category']           #bracket names are same as left
				
				Task(user=request.user,description=Description, category=Category).save()   #first para on the left are from model
				
				tasks_obj = Task.objects.select_related().filter(user=request.user)
				
				return render(request, 'tasks/view_task_list.html', {"alltasks": tasks_obj} )

		return render(request,'tasks/add_task.html',{"taskform":add_task_form})

#@login_required(login_url='/login/')
def edit_task(request):
		list=Task.objects.get(id=request.GET['e_id'])
		data={}
		array={}
		array['Ids']=list.id
		array['Description']=list.description
		array['Category']=list.category
		array['Completed']=list.completed

		forms=edit_task_form(request.POST or None,initial=array)
		data['forms']=forms

		return render(request,'tasks/edit_task.html',data)
	
#@login_required(login_url='/login/')
def delete_tasks(request):
	ddata = Task.objects.get(id=request.GET['delete'])
	ddata.delete()
	try:
		
		tasks_obj = Task.objects.select_related().filter(user=request.user)
		return render(request, 'tasks/view_task_list.html', {"alltasks": tasks_obj})
	except Task.DoesNotExist:
		tasks_obj = None
	return render(request, 'tasks/view_task_list.html', {"alltasks": tasks_obj})
	   #first para on the left are from model
				
	
	