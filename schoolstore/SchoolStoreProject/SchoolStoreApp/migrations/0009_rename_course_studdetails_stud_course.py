# Generated by Django 4.2.4 on 2023-09-06 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolStoreApp', '0008_rename_stud_course_studdetails_course_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studdetails',
            old_name='course',
            new_name='stud_course',
        ),
    ]