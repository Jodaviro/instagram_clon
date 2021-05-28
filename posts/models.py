"""Posts models."""

#Django
from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

# Create your models here.

#para importar el modelo profile, en el siguiente ejemplo lo hicimos de la sguiente forma
class Post(models.Model):
    """Post model class for post"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to='posts/photo')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')

    @classmethod
    def like_post(cls, user, another_user):
        object= cls.objects.get(user=user)
        object.likes.add(another_user)

    def likes_count(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.title} by @{self.user}'


class Comment(models.Model):
    """Comment model for posts"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField(default="", max_length=300,)
    likes = models.ManyToManyField(User, blank=True, related_name='like')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def likes_count(self):
        return self.likes.count()

    def __str__(self):
        return f'by {self.user.username}: {self.text}'