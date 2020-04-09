from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Task
from tasks.forms import add_task_form
# Create your views here.
def tasks1(request):
	#return HttpResponse("Hello World!")
	if (request.method == "POST"):
		add_task = addtask(request.POST)
        
		if (join_form.is_valid()):
			user = add_task.save()
			user.save()
            # Success! Redirect to home page.
			return redirect("/")
		else:
			print(join_form.errors)
	return render(request, 'tasks/view_task_list.html')

def tasks(request):
	tasks_obj = Task.objects.all
	return render(request, 'tasks/view_task_list.html', {"alltasks": tasks_obj} )

def clean(self):
    cleaned_data = super(CreateJobOpportunityForm, self).clean()
    end_date = cleaned_data['end_date']
    start_date = cleaned_data['start_date']
    # do your cleaning here
    return cleaned_data

def add_task(request):
	if (request.method == 'POST'):
		form = add_task_form(request.POST);
		if (form.is_valid()):
			Description = form.cleaned_data['Description']  #names on the left are from form
			Category = form.cleaned_data['Category']           #bracket names are same as left
			Task(description=Description, category=Category).save()   #first para on the left are from model
	return render(request,'tasks/add_task.html',{"taskform":add_task_form})