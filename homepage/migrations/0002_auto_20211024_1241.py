# Generated by Django 3.2.8 on 2021-10-24 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='dateadded',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(null=True),
        ),
    ]