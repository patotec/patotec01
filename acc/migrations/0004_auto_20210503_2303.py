# Generated by Django 2.2 on 2021-05-03 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0003_auto_20210502_1417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='discription_about_user',
            new_name='message',
        ),
        migrations.AddField(
            model_name='customuser',
            name='salary',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
