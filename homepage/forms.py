from django import forms


# fields needed: name, desc, owner, link, status, tags
# bare min needed: name, desc, tags, links
class ProjectForms(forms.Form):
    project_name = forms.CharField(label='Project Name', max_length=200, required=True)
    description = forms.CharField(label='Description', max_length=1000, required=True)
    email = forms.EmailField(label='Email', required=True)

    lookingforpeople = forms.BooleanField(label='Looking For People',required=True)

    image = forms.ImageField(label="Image", required=False)

    project_URL = forms.URLField(label='Project URL', required=False)
    tags = forms.CharField(label='Tags', required=False)
    