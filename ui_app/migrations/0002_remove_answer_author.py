# Generated by Django 2.0.3 on 2018-03-12 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ui_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
    ]
