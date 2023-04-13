from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pic', default='default.jpg')
    email = models.EmailField(max_length=255, unique=True)
    
    def __str__(self) -> str:
        return self.username
    