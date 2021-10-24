from django import forms


# fields needed: name, desc, owner, link, status, tags
# bare min needed: name, desc, tags, links
class ProjectForms(forms.Form):
    project_name = forms.CharField(label='Project Name', max_length=100)
    project_URL = forms.URLField(label='Project URL')
    description = forms.CharField(label='Description', max_length=800)
    tags = forms.CharField(label='tags')
    