from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.forms import forms

from homepage.forms import ProjectForms

from homepage.models import Project

# Create your views here.
def index(request):
    featured_projects = Project.objects.order_by('-votes')[:3]
    seeking_volunteers = Project.objects.order_by('-dateadded')[:3]
    context = {
    "featured_projects": featured_projects,
    "seeking_volunteers": seeking_volunteers
    }
    return render(request, 'homepage/homepage.html', context)

def allprojects(request):
    #Should make a get request and search for project using tags 
    return render(request, 'homepage/browse_projects.html')

def viewproject(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {"project":project}
    return render(request, 'homepage/view_project.html', context)

def createproject(request):
    form = ProjectForms(request.POST)
    return render(request, 'homepage/create_project.html', {'form': form})

def postsubmit(request):
    #TODO: instead redirect to the project's page
    #use the form response thing
    return render(request, 'homepage/post_submit.html')

def get_project_info(request):
    if request.method == 'POST':
        form = ProjectForms(request.POST)
        if form.is_valid():
                return HttpResponseRedirect('/thanks/')
        else:
            form = ProjectForms() # wrong input, just reload
            return render(request, 'homepage/create_project.html', {'form': form})
        