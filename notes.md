# Just build it!

- Github Actions: https://medium.com/intelligentmachines/github-actions-basics-40a4d9b417f8
- Github Actions for Django: https://medium.com/intelligentmachines/github-actions-end-to-end-ci-cd-pipeline-for-django-5d48d6f00abf
- Awesome Django Official Tutorial: https://docs.djangoproject.com/en/3.2/intro/tutorial02/


## TODO
- ~~Add voting functionality --> Youssef~~
- A page to view a single Project --> improve to display other stuff --> possibly display image
- Add links from homepage and all projects to individual project pages
- Add Tags

- submit project and make presentation

## Notes
- Urls file
- 'polls.apps.PollsConfig'
- views
- admin.site.register(Question)
- python manage.py makemigrations polls
- python manage.py migrate
- python manage.py check
- Remember to save values
- Add __str__(self) methods
- https://docs.djangoproject.com/en/3.2/intro/tutorial03/
- python manage.py createsuperuser


- Playground: python manage.py shell
- Ids are accessible after saving
- Question.objects.filter(id=1)
- Question.objects.filter(question_text__startswith='What')
- Question.objects.get(pub_date__year=current_year)
- Question.objects.get(pk=1)
- question.choice_set.all()
- choice.question
- question.choice_set.count()
- Choice.objects.filter(question__pub_date__year=current_year)
- choice.delete()
- 
    - Asks for username, email, password
- Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])


- >>> q.choice_set.create(choice_text='Not much', votes=0)


```python
>>> from polls.models import Choice, Question  # Import the model classes we just wrote.

# No questions are in the system yet.
>>> Question.objects.all()
<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id
1

# Access model field values via Python attributes.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```