# Generated by Django 3.2 on 2022-06-12 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20220612_2230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'faculty', 'verbose_name_plural': 'faculties'},
        ),
    ]