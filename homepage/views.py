from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'homepage/homepage.html')

def allprojects(request):
    return render(request, 'homepage/browse_projects.html')

def createproject(request):
    return render(request, 'homepage/create_project.html')