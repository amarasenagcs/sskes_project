# Generated by Django 4.0.2 on 2022-09-24 18:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sskes_app', '0013_alter_course_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='answer',
            field=models.FileField(blank=True, null=True, upload_to='answers/'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='grade',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='updated_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
