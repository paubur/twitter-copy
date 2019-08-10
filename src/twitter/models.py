from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tweet(models.Model):
    content = models.TextField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}..".format(self.user.username, self.content[:10])
