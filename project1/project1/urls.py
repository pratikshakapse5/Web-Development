"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views as app1_views
from core import views as core_views
from tasks import views as tasks_views
from journal import views as journal_views
from budget import views as budget_views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('about/', core_views.about, name='about'),
	path('home/',core_views.home, name='home'),
	path('',core_views.home,name='home'),
	path('journal/',journal_views.journal,name='journal'),
	path('budget/',budget_views.budget,name='budget'),
	path('tasks/',tasks_views.tasks,name='tasks'),
	path('project1/templates/core/pratiksha.jpg',core_views.about,name='about'),
	path('add_task/',tasks_views.add_task,name='add_task'),
	path('edit_task',tasks_views.edit_task,name='edit_task'),
	path('edit_budget/',budget_views.edit_budget,name='edit_budget'),
	path('delete_tasks',tasks_views.delete_tasks,name='delete_tasks'),
	path('add_budget/',budget_views.add_budget,name='add_budget'),
	path('delete_budget/',budget_views.delete_budget,name='delete_budget'),
	
	path('add_journal/',journal_views.add_journal,name='add_journal'),
	path('edit_journal',journal_views.edit_journal,name='edit_journal'),
	path('delete_journal',journal_views.delete_journal,name='delete_journal'),
	#path('view_budget_list/',budget_views.view_budget_list,name='view_budget_list'),
    path('logout/', core_views.user_logout, name='user_logout'),
	path('login/',core_views.user_login,name='user_login'),
	path('join/',core_views.join,name='join')
]
