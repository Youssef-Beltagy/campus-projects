from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.allprojects, name='allprojects'),
    path('create/', views.createproject, name='createproject'),
    path('view/<int:project_id>', views.viewproject, name='viewproject'),
]