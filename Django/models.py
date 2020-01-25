from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.TextField()
    
    def __str__(self):
      return self.name


class Group(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    description = models.TextField()
    name = models.TextField(unique=True)
    private = models.BooleanField(default=True)

    def __str__(self):
      return self.name


class Post(Likable):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type', 'object_id')

    shares = models.ManyToManyField(User, blank=True)
    author = models.OneToOneField(User, on_delete=models.SET_NULL, primary_key=True)
    title = models.TextField()
    body = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
      return self.title


class Likable(models.Model):
    likes = models.ManyToManyField(User, blank=True)


class Discussion(models.Model):
    profile = models.OneToOneField(Group)
    posts = GenericRelation(Post)


class Photos(models.Models):
    profile = models.OneToOneField(Group)    
    posts = GenericRelation(Post)


class Comment(Likable):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    reply_to = models.ForeignKey('self', blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
      return f'Comment: {self.text} for post {self.post}.'
