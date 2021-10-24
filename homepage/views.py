from django.http import response
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
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
    """Sends the form and processes the reply"""
    if request.method == 'GET': # If the form has been submitted...
        form = ProjectForms()
        return render(request, 'homepage/create_project.html', {'form': form})
    project = Project()
    
    try:
        project.name = request.POST['project_name']
        project.description = request.POST['description']
        project.contact_email = request.POST['email']

        project.lookingforpeople = (request.POST['lookingforpeople'] == "on")  

        project.image = request.POST["image"]

        project.url = request.POST['project_URL']

        tags = request.POST['tags'] # TOBE used later

        project.save()
        

    except (KeyError):
        # Redisplay the question voting form.
        return HttpResponse("Submission Failed")

    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect('/view/{}'.format(project.id))    
        