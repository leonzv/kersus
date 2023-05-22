from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='category_profile_pics', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Participant(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='participant_profile_pics', blank=True)
    category = models.ForeignKey(Category, related_name='participants', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name