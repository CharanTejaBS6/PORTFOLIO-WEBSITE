# Generated by Django 5.0 on 2024-03-07 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PApp', '0003_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
            ],
        ),
    ]
