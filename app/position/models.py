from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from app.user.models import CreatedUpdatedBase


class Position(CreatedUpdatedBase):
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=200)
    user = models.ManyToManyField(User)

    class Meta:
        db_table = 'position'

    def __str__(self):
        return self.name
