# Generated by Django 4.2.4 on 2023-09-06 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolStoreApp', '0007_alter_studdetails_purpose_delete_purposes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studdetails',
            old_name='stud_course',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='studdetails',
            old_name='stud_dept',
            new_name='department',
        ),
    ]