from django.db import models
from model_utils.models import TimeStampedModel

from users.models import User


class Posts(TimeStampedModel):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    text = models.CharField(max_length=200)

    class Meta:
        db_table = 'POSTS'

    def __str__(self):
        return self.text
