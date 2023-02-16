from django.db.models import ForeignKey, CharField, CASCADE
from model_utils.models import TimeStampedModel

from posts.models import Posts
from users.models import User


# Create your models here.
class Comment(TimeStampedModel):
    created = ForeignKey(User, on_delete=CASCADE)
    title = CharField(max_length=200)
    post = ForeignKey(Posts, related_name="comments", on_delete=CASCADE)

    def __str__(self):
        return f'{self.title}---{self.id}'
