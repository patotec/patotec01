# Generated by Django 2.2 on 2021-05-06 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0006_auto_20210505_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
