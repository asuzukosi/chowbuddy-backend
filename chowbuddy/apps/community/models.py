from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='community_profile')
    members = models.ManyToManyField(get_user_model(), related_name='community_members')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    text = models.CharField(max_length=100)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.text} by {self.author} in {self.community}"
    
