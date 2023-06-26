from django.db import models


# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, null=True)
    duration = models.DurationField(null=True)
    steps = models.JSONField(null=True)
    image = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.name
