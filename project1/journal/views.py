from django.shortcuts import render
from django.http import HttpResponse
from journal.models import Journal
from journal.forms import add_journal_form
from journal.forms import edit_journal_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from core.models import UserProfileCore
# Create your views here.

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect("home")


def journal(request):
	if not request.user.is_authenticated:
		return render(request, 'core/login.html')
	else:
		if request.method == 'POST':
			t_form = edit_journal_form(request.POST)
			if(t_form.is_valid()):
				
				task_list_data = Journal.objects.get(id=t_form.cleaned_data["Ids"])
				task_list_data.description = t_form.cleaned_data["Description"]
				task_list_data.entry = t_form.cleaned_data["Entry"]
				task_list_data.save()
	
	journal_obj = Journal.objects.select_related().filter(user=request.user)
	return render(request, 'journal/view_journal_list.html', {"alljournal": journal_obj} )


def add_journal(request):
	if (request.method == 'POST'):
		form = add_journal_form(request.POST);
		if (form.is_valid()):
			Description = form.cleaned_data['Description']  #names on the left are from form
			Entry=form.cleaned_data['Entry']       #bracket names are same as left
			Journal(user=request.user,description=Description, entry=Entry).save()   #first para on the left are from model
				
			journal_obj = Journal.objects.select_related().filter(user=request.user)
			return render(request,'journal/view_journal_list.html',{"alljournal":journal_obj})
	
	return render(request,'journal/add_journal.html',{"journalform":add_journal_form})

def edit_journal(request):
		list=Journal.objects.get(id=request.GET['e_id'])
		data={}
		array={}
		array['Ids']=list.id
		array['Description']=list.description
		array['Entry']=list.entry
		forms=edit_journal_form(request.POST or None,initial=array)
		data['forms']=forms

		return render(request,'journal/edit_journal.html',data)


def delete_journal(request):
	ddata = Journal.objects.get(id=request.GET['delete'])
	ddata.delete()
	try:
		
		tasks_obj = Journal.objects.select_related().filter(user=request.user)
		return render(request, 'journal/view_journal_list.html', {"alljournal": tasks_obj})
	except Journal.DoesNotExist:
		tasks_obj = None
	return render(request, 'journal/view_journal_list.html', {"alljournal": tasks_obj})
	
	