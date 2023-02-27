from django.db import models
from django.db.models import Model
from model_utils.models import TimeStampedModel

from users.models import User


# Create your models here.

class Friends(TimeStampedModel):
    friend = models.BooleanField(default=False)
    transmitter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transmitted')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received')


    def __str__(self):
        return f'transmitte: {self.transmitter.email} -------- received: {self.receiver.email}---friend: {self.friend}'
