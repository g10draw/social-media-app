from django.db import models

from auth_manager.models import CustomUser

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post_text = models.TextField()
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(CustomUser, related_name='my_likes')

    def __str__(self):
        return self.post_text


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)


class Follow(models.Model):
    follower = models.ForeignKey(CustomUser, related_name='following', 
                on_delete=models.CASCADE)
    following = models.ForeignKey(CustomUser, related_name='followers',
                on_delete=models.CASCADE)