# Generated by Django 4.0.2 on 2022-09-22 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sskes_app', '0010_parentconnect_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='parentconnect',
            name='status',
            field=models.CharField(choices=[('accept', 'accept'), ('reject', 'reject'), ('pending', 'pending')], default='pending', max_length=20),
        ),
    ]
