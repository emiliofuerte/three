# Generated by Django 3.2 on 2022-12-06 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20221206_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('fr', 'French')], default='en', max_length=2),
        ),
    ]