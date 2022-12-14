from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
User=get_user_model()
# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    uid=models.IntegerField()
    bio=models.TextField(blank=True)
    profile_img=models.ImageField(upload_to='profile_images',default='blank_profile.png')
    location=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.CharField(max_length=100)
    text=models.CharField(max_length=1000)
    created_at=models.DateTimeField(default=datetime.now)
    no_of_likes=models.IntegerField(default=0)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    user=models.CharField(max_length=100)
    text=models.CharField(max_length=1000)
    created_at=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '%s - %s' %{self.post.text,self.user}



