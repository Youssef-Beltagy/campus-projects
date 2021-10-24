from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import forms

from homepage.forms import ProjectForms
# Create your views here.
def index(request):
    return render(request, 'homepage/homepage.html')

def allprojects(request):
    return render(request, 'homepage/browse_projects.html')

def createproject(request):
    form = ProjectForms(request.POST)
    return render(request, 'homepage/create_project.html', {'form': form})

def postsubmit(request):
    return render(request, 'homepage/post_submit.html')


def get_project_info(request):
    if request.method == 'POST':
        form = ProjectForms(request.POST)
        if form.is_valid():
                return HttpResponseRedirect('/thanks/')
        else:
            form = ProjectForms() # wrong input, just reload
            return render(request, 'homepage/create_project.html', {'form': form})
        