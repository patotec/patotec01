# Generated by Django 2.2 on 2021-05-02 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0002_auto_20210502_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='fullname',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='')),
                ('occupation', models.CharField(blank=True, max_length=200)),
                ('discription_about_user', models.CharField(blank=True, max_length=2000)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved')], default='pending', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]