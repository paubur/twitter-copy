from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tweet(models.Model):
    content = models.TextField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}..".format(self.user.username, self.content[:10])


class Message(models.Model):
    message = models.TextField()
    sender = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="sender")
    receiver = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="receiver")
    date_sent = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
