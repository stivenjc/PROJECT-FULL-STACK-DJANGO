from django.db import models

from posts.models import Posts
from users.models import User


# Create your models here.

class Likes(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'LIKES'

    def __str__(self):
        return str(self.post)
