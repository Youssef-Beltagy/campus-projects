from django.db import models
from django.db.models.fields import DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date

# Create your models here.

#https://github.com/jazzband/django-taggit
#https://dev.to/coderasha/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704
#https://realpython.com/django-templates-tags-filters/


#TODO: ADD User Foreign Key
#TODO: Add Project Status choice: WONTFIX
#TODO: ADD expected commitment choice: WONTFIX
#TODO: ADD tags

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    contact_email = models.EmailField(null=True)

    lookingforpeople = models.BooleanField(default=True)

    
    url = models.URLField(null=True)
    image = models.ImageField(null=True)

    votes = models.PositiveBigIntegerField(default=0)
    dateadded = models.DateField(default=date.today)


    def __str__(self):
        return self.name
