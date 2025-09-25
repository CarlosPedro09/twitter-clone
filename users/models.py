from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(max_length=280, blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    def __str__(self):
        return self.username

class Follow(models.Model):
    follower = models.ForeignKey(
        'CustomUser', on_delete=models.CASCADE, related_name='following'
    )
    following = models.ForeignKey(
        'CustomUser', on_delete=models.CASCADE, related_name='followers'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower.username} segue {self.following.username}"
