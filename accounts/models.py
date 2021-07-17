from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
    phno =models.IntegerField(default=999999999)
    dob = models.DateField(default=timezone.now)
    state = models.CharField(default='Andhra Pradesh',max_length=100)
    university = models.CharField(default='Sastra',max_length=100)
    sem = models.IntegerField(default=5)

    def __str__(self):
        return f'{self.user.username} Profile'