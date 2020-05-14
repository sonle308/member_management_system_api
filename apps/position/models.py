from django.db import models
from django.contrib.contenttypes.models import ContentType
from apps.user.models import CreatedUpdatedBase
from django.contrib.auth import get_user_model

User = get_user_model()

class Position(CreatedUpdatedBase):
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=200)
    user = models.ManyToManyField(User)

    class Meta:
        db_table = 'position'

    def __str__(self):
        return self.name
