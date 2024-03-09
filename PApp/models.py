from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    commencement_date = models.DateField()
    # Change this line to store the image URL
    image_url = models.URLField(
        default='https://example.com/default_image.jpg')

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField()

    def __str__(self):
        return self.name


class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.name
