from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  content  = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
      created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='shares')
    created_at = models.DateTimeField(auto_now_add=True)
