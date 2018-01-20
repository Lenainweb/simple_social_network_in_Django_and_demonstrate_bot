from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', 'on_delete')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    likes = models.IntegerField(default=0)
    unlikes = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# class LikesUnlikes(models.Model):
#     post = models.ForeignKey('Post', 'on_delete')
#     likes = models.IntegerField(default=0)
#     unlikes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.likes + '/' +  self.unlikes


