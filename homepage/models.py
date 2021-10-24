from django.db import models
from django.db.models.fields import URLField
from django.db.models.fields.files import ImageField

# Create your models here.

#https://github.com/jazzband/django-taggit
#https://dev.to/coderasha/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704
#https://realpython.com/django-templates-tags-filters/

# TODO: Continue
# class Project(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     votes = models.PositiveBigIntegerField(default=0)
#     url = models.URLField()
#     contact_email = models.EmailField()
#     image = ImageField()
#     models.ForeignKey(User, on_delete=models.CASCADE)

# class Choice(models.Model):
#     question = 
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
