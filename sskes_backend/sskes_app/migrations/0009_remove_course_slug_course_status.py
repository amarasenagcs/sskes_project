# Generated by Django 4.0.2 on 2022-09-21 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sskes_app', '0008_lesson_content_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='slug',
        ),
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]