from django.db import models
from django.contrib.auth.models import User
from exercise.models import Exercise

# User._meta.get_field('email')._unique = False
# User._meta.get_field('email').blank = True
# User._meta.get_field('email').null = True

# Create your models here.
class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images', null=True)
    exercise_join = models.ForeignKey(Exercise, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username
