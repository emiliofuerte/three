# Generated by Django 3.2 on 2022-12-18 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_author_secret_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='secret_name',
        ),
    ]
