from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    #id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='POSTS')
    date_posted = models.DateTimeField(default=timezone.now,editable=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.location} {self.id}'

class comment(models.Model):
    #id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    commenter_name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.id} {self.commenter_name.username}'