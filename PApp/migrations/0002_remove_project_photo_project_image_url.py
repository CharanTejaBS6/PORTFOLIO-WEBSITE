# Generated by Django 5.0 on 2024-03-05 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='photo',
        ),
        migrations.AddField(
            model_name='project',
            name='image_url',
            field=models.URLField(default='https://example.com/default_image.jpg'),
        ),
    ]
