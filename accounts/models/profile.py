from django.db import models
from .accounts import User

class Profile(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    image = models.ImageField(upload_to='profile', null=True, blank=True)
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.email
    
