from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    profile_pic = models.ImageField(upload_to='category_profile_pics', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Categories'
  
class Participant(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='participant_profile_pics', blank=True)
    category = models.ForeignKey(Category, related_name='participants', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name