# Generated by Django 4.1 on 2022-08-27 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_content', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='rank',
            new_name='rate',
        ),
    ]
