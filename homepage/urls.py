from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.allprojects, name='allprojects'),
    path('submit/', views.createproject, name='createproject'),
    path('thanks/', views.postsubmit, name='postsubmit'),
    path('your-project/', views.get_project_info, name='your-project')
]