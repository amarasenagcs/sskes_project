# Generated by Django 4.0.2 on 2022-09-22 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParentConnect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('accept', 'accept'), ('reject', 'reject'), ('pending', 'pending')], default='pending', max_length=20)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='parent_student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
